from django.shortcuts import get_object_or_404, render
from .models import Products_listing
from django.contrib.auth.decorators import login_required

# Create your views here.
def home(request):
    products = Products_listing.objects.all()
    return render(request, 'pages/index.html',{'products':products})

def search(request):
    if request.method == 'POST':
        searched = request.POST['searched']
        products = Products_listing.objects.filter(product_name__contains =searched)
        return render(request, 'pages/index.html',{'searched':searched, 'products':products})
    
    else:
        return render(request, 'pages/index.html')
    

@login_required(login_url='login')   
def product(request, product_id):
    products = get_object_or_404(Products_listing, pk=product_id)
    context = {
        'products': products
    }
    return render(request,'pages/product.html',context)