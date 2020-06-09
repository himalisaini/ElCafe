from django.shortcuts import render , redirect
from .models import Item , BillingModel
from .forms import BillingForm
from django.core.paginator import Paginator
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.template import loader
import pdfkit
from django.http import HttpResponse

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


@login_required
def billing(request):
    if request.method == "POST":
        form = BillingForm(request.POST)
        if form.is_valid():
            order = form.save()
            nl = '\n'
            messages.success(request, f"Order placed successfully!{nl}Please check your mail for confirmation!{nl}"
                                      f"Check the Orders section for the receipt!"
                                      f"{nl}Keep ordering!!")
            return redirect('index')
    else:
        form = BillingForm()
    return render(request, 'shop/billing.html', {'form': form})


@login_required
def order_details(request,id):
    obj = BillingModel.objects.get(pk=id)
    return render(request, 'shop/order_details.html', {'obj': obj})


def reviews(request):
    return render(request,'shop/review.html')


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
