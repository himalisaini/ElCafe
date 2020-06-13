from django.shortcuts import render , redirect
from .models import Item , BillingModel , Review
from .forms import BillingForm
from django.core.paginator import Paginator
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.template import loader
import pdfkit
from django.http import HttpResponse
from django.views.generic import DetailView , CreateView , UpdateView , DeleteView
from django.contrib.auth.mixins import LoginRequiredMixin , UserPassesTestMixin
from django.contrib.messages.views import SuccessMessageMixin
# Create your views here.


def index(request):
    item_objects = Item.objects.all()
    item_name = request.GET.get('item_name')

    #adding search functionality
    if item_name != '' and item_name is not None:
        item_objects = item_objects.filter(title__icontains=item_name)

    #adding pagination
    paginator = Paginator(item_objects,6)
    page = request.GET.get('page')
    item_objects = paginator.get_page(page)

    return render(request, 'shop/index.html', {'item_objects': item_objects})


def detail(request,id):
    item_obj = Item.objects.get(id=id)
    return render(request,'shop/detail.html',{'item_obj':item_obj})


@login_required
def checkout(request):
    return render(request,'shop/checkout.html')


class BillingCreate(LoginRequiredMixin,CreateView):
    model = BillingModel
    fields = ['first_name','last_name','email','phone_number','address','payment_mode']
    template_name = 'shop/billing.html'

    def form_valid(self, form):
        form.instance.customer = self.request.user
        form.instance.cart_items = self.request.POST.get('item_list',"")
        form.instance.item_quantity = self.request.POST.get('item_quantity', "")
        form.instance.item_price = self.request.POST.get('item_list_price', "")
        form.instance.item_disc = self.request.POST.get('item_list_disc', "")
        form.instance.total_price = self.request.POST.get('total_price', "")
        form.instance.discount_applied = self.request.POST.get('disc_applied', "")
        form.instance.final_amount = self.request.POST.get('final_amount', "")
        return super().form_valid(form)


@login_required
def order_details(request,id):
    obj = BillingModel.objects.get(pk=id)
    return render(request, 'shop/order_details.html', {'obj': obj})


def reviews(request):
    posts = Review.objects.all()
    context = {
        'posts' : posts
    }
    return render(request,'shop/review.html',context)


@login_required
def myorders(request):
    obj = BillingModel.objects.all()
    obj = obj.filter(customer=request.user.pk)

    return render(request,'shop/myorders.html',{'obj':obj})


class ReviewDetail(DetailView):
    model = Review
    template_name = 'shop/review_detail.html'


class ReviewCreate(LoginRequiredMixin,SuccessMessageMixin,CreateView):
    model = Review
    fields = ['title','content']
    success_url = '/review/'
    success_message = "Your review has been posted!"
    template_name = 'shop/review_form.html'

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)


class ReviewUpdate(LoginRequiredMixin,UserPassesTestMixin,SuccessMessageMixin,UpdateView):
    model = Review
    fields = ['title','content']
    success_url = '/review/'
    success_message = "Your review has been updated!"
    template_name = 'shop/review_form.html'

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)

    def test_func(self):
        review = self.get_object()
        if self.request.user == review.author:
            return True
        return False


class ReviewDelete(LoginRequiredMixin,UserPassesTestMixin,SuccessMessageMixin,DeleteView):
    model = Review
    success_url = '/review/'
    success_message = "Your review has been deleted!"
    template_name = 'shop/review_confirm_delete.html'

    def test_func(self):
        review = self.get_object()
        if self.request.user == review.author:
            return True
        return False


def receipt(request,id):
    obj = BillingModel.objects.get(pk=id)
    template = loader.get_template('shop/receipt.html')
    html = template.render({'obj':obj})
    options = {
        'page-size':'Letter',
        'encoding':"UTF-8",
    }
    pdf = pdfkit.from_string(html,False,options)
    response = HttpResponse(pdf,content_type='application/pdf')
    response['Content-Disposition'] = 'attachment'

    return response


