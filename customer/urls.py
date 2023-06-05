from django.urls import path,include
from customer.views import*
urlpatterns = [
    path('get-customer',GetCustomereView.as_view()),
    path('get-address',GetAddressView.as_view()),
    
]
