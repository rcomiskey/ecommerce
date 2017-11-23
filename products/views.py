from django.shortcuts import render
from .models import Product

# Create your views here.
def viewproducts(request):
    products = Product.objects.all()
    return render(request, 'viewproducts.html', {'products': products})
    
def do_search(request):
    products = Product.objects.filter(name__icontains=request.GET['q'])
    return render(request, 'viewproducts.html', {'products': products})
