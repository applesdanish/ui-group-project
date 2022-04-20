from django.shortcuts import render

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