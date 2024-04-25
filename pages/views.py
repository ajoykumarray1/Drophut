from django.shortcuts import render
from .models import Products_listing

# Create your views here.
def home(request):
    products = Products_listing.objects.all()
    return render(request, 'pages/index.html',{'products':products})