from django.urls import path,include
from customer.views import*
urlpatterns = [
    path('get-customer',GetCustomereView.as_view()),

    
]
