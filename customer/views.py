from django.shortcuts import render
from customer.models import*
from rest_framework import status
from rest_framework.views import APIView
from rest_framework.response import Response
from customer.serializers import* 
# Create your viwes here.
class GetCustomereView(APIView):
    def get(self,request):
        instance = Customer.objects.all()
        serializer = GetCustomerSerializers(instance,many=True)
        return Response(serializer.data)
    
    
    def post(self,request): 
        params =request.data
        print("data >>>>>>>",params)
        ser =GetCustomerSerializers(data=params)
        ser.is_valid(raise_exception=True)
        ser.save()
        return Response({"msg":"save sucessfully!!!"})
    
class GetAddressView(APIView):  
    def get(self,request):
        instance = CustomerAddress.objects.all()
        serializer = GetAddressSerializers(instance,many = True)
        return Response(serializer.data)
    
class CustomerDetailAddressView(APIView):
    def get(self,request,pk):
        instance = Customer.objects.filter(id = pk)
        ser = CustomerDetailsAddress(instance,many = True)
        return Response(ser.data)