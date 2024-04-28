from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.contrib.auth import authenticate,logout,login
from django.contrib import messages,auth
from django.contrib.auth.models import User
from django.shortcuts import redirect

# Create your views here.
def register(request):
    if request.method == 'POST':
        first_name = request.POST['first_name']
        last_name = request.POST['last_name']
        username = request.POST['username']
        email = request.POST['email']
        password = request.POST['password']
        password2 = request.POST['password2']

        if password == password2:
            if User.objects.filter(username=username).exists():
                messages.error(request,"user name dosen't  exist")
            else:
                if  User.objects.filter(email=email).exists():
                    messages.error(request,"Email is being used")
                    return redirect('register')
            
                else:
                    user = User.objects.create_user(email=email,password=password,first_name=first_name, last_name=last_name, username=username)
                    user.save()
                    messages.success(request, 'Your are  now registered and can log in')
                    return redirect('login')
        else:
            messages.error(request,'Passwords do not match')
            return redirect('register')
    else:
        return render(request, 'accounts/register.html', )

def user_login(request):
    if request.method == "POST":
        username =  request.POST["username"]
        password =  request.POST["password"]

        user = authenticate(username = username, password=password)

        if user is not None:
            login(request, user)
            messages.info(request, "You are successfully loged in")
            return redirect("home")
        else:
            messages.warning(request, "Username or Password is incorrect")
            return redirect("login")
    else:
        return render(request, 'accounts/login.html')

def user_logout(request):
    logout(request)
    return HttpResponseRedirect('/')