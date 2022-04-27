from django.shortcuts import render
import ctypes  # An included library with Python install.   
from .models import *
from django.http import JsonResponse
import json

# Create your views here.
def store(request, *args, **kwargs):
    products = Product.objects.all()
    context = {'products':products}
    return render(request, 'store.html', context)

def cart(request, *args, **kwargs):
    
    if request.user.is_authenticated:
        customer = request.user.customer
        order, created = Order.objects.get_or_create(customer=customer, complete=False)
        items = order.orderitem_set.all()
    else:
        items = []
        order = {'get_cart_total':0, 'get_cart_items':0}

    context = {'items':items, 'order':order}
    return render(request, 'cart.html', context)

def checkout(request, *args, **kwargs):
    if request.user.is_authenticated:
        customer = request.user.customer
        order, created = Order.objects.get_or_create(customer=customer, complete=False)
        items = order.orderitem_set.all()
    else:
        items = []
        order = {'get_cart_total':0, 'get_cart_items':0}

    context = {'items':items, 'order':order}
    return render(request, 'checkout.html', context)

def login(request, *args, **kwargs):
    context = {}
    return render(request, 'login.html', context)

def signup(request, *args, **kwargs):
    context = {}
    return render(request, 'signup.html', context)

def faq(request, *args, **kwargs):
    context = {}
    return render(request, 'faq.html', context)

def reviews(request, *args, **kwargs):
    context = {}
    return render(request, "reviews.html", context)

def createAccount(request):
    if request.method == "POST":
        username = request.POST["username"];
        password = request.POST["password"];
        password2 = request.POST["password2"];
        ctypes.windll.user32.MessageBoxW(0, username + " " + password + " " + password2, "Username/Password", 1)

def faq_detail_view(request):
    n = 0
    faq_list = []
    while True:
        n += 1
        try:
            obj = Faq.objects.get(id=n)
            faq_list.append(obj.question + " " + obj.response)
            #context[obj.question] = obj.response
        except:
            break
    context = {
        "faq_dict": faq_list
    }
    return render(request, "faq.html", context)

def updateItem(request):
    data = json.loads(request.data)
    productId = data['productId']
    action = data['action']

    print('action:', action)
    print('product:', product)
    return JsonResponse('Item was added', safe=False)