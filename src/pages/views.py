from django.shortcuts import render
import ctypes  # An included library with Python install.   

# Create your views here.
def store(request, *args, **kwargs):
	context = {}
	return render(request, 'store.html', context)

def cart(request, *args, **kwargs):
	context = {}
	return render(request, 'cart.html', context)

def checkout(request, *args, **kwargs):
	context = {}
	return render(request, 'checkout.html', context)

def login(request, *args, **kwargs):
    context = {}
    return render(request, 'login.html', context)

def signup(request, *args, **kwargs):
    context = {}
    return render(request, 'signup.html', context)

def createAccount(request):
    if request.method == "POST":
        username = request.POST["username"];
        password = request.POST["password"];
        password2 = request.POST["password2"];
        ctypes.windll.user32.MessageBoxW(0, username + " " + password + " " + password2, "Username/Password", 1)
