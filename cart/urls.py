from django.contrib import admin
from django.urls import path
from django.urls.conf import include

from cart import views

urlpatterns = [
    path('',views.cartIndex,name="cartIndex"),    
]
