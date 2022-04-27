"""ecommerce URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from pages.views import store, cart, checkout, login, signup, reviews, pikachu_hat, straw_hat, hulk_hands, costume, fan, headphones, speaker, earphones, roomba, fun_socks
from faq.views import faq_detail_view

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', store, name="store"),
    path('cart/', cart, name="cart"),
    path('checkout/', checkout, name="checkout"),
    path('login/', login, name='login'),
    path('signup/', signup, name='signup'),
    path('faq/', faq_detail_view, name='faq'),
    path('reviews', reviews, name="reviews"),

    path('pikachu_hat', pikachu_hat, name="pikachu_hat"),
    path('straw_hat', straw_hat, name="straw_hat"),
    path('hulk_hands', hulk_hands, name="hulk_hands"),
    path('costume', costume, name="costume"),
    path('fan', fan, name="fan"),
    path('headphones', headphones, name="headphones"),
    path('speaker', speaker, name="speaker"),
    path('earphones', earphones, name="earphones"),
    path('roomba', roomba, name="roomba"),
    path('fun_socks', fun_socks, name="fun_socks"),

]
