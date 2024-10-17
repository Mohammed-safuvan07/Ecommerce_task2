from django.shortcuts import render, get_object_or_404
from . models import Category,Product

# Create your views here.
def demo(request):
    return render(request,'hello.html')

def AllProdCat(request,c_slug=None):
    products = None
    c_page = None
    if c_slug != None:
        c_page = get_object_or_404(Category,slug=c_slug)
        products = Product.objects.all().filter(category=c_page,available=True)
    else:
        products = Product.objects.all().filter(available=True)
    return render(request,'category.html',{'category':c_page,'products':products})

def ProdDetail(request,c_slug,product_slug):
    try:
        product = Product.objects.get(category__slug=c_slug,slug=product_slug)
    except Exception as e:
        raise e
    return render(request,'product.html',{'product':product})