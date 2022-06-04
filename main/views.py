from django.shortcuts import render

# Create your views here.
from .models import Category, Product

def main_page(request):
    categories= Category.objects.all()
    products= Product.objects.all()
    context={
        'categories': categories,
        'products': products
    }
    return render(request, 'main_page.html', context)

def category_sort(request,id):
    products =Product.objects.filter(categories=id)
    context ={"products": products}
    return render(request,'categories_product.html',context)
