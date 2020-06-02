from django.shortcuts import render
from .models import Item
from django.core.paginator import Paginator
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
    