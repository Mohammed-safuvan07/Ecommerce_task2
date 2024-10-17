from django.db.models import Q
from django.shortcuts import render
from Ecomapp.models import Product

# Create your views here.
def Searches(request):
    query = None
    products = None
    if 'q' in request.GET:
        query = request.GET.get('q')
        products = Product.objects.all().filter(Q(name__icontains=query) | Q(desc__icontains=query))
    return render(request, 'search.html', {'query': query, 'products': products})