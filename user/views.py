from django.shortcuts import render, redirect
from django.contrib.auth.models import auth
from django.contrib.auth import authenticate

from .forms import CreateUserForm, LoginForm
# Create your views here.

def home(request):
    return render(request,'user/index.html')

# register
def register(request):
    form = CreateUserForm()

    if request.method == 'POST':
        form = CreateUserForm(request.POST)

        if form.is_valid():
            form.save()
            return redirect('home')
    
    return render(request, 'user/register.html', context={'form': form})
    

def login(request):
    form = LoginForm()
    requestBody = request.POST

    if request.method == "POST":
        form = LoginForm(request, requestBody)

        if form.is_valid():
            username = requestBody.get('username')
            password = requestBody.get('password')

            user = authenticate(request, username=username, password=password)

            if user is not None:
                auth.login(request, user)

    return render(request, 'user/userLogin.html', context={'form': form})

            
