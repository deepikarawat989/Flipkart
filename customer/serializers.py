from rest_framework import serializers
from customer.models import*

class GetCustomerSerializers(serializers.ModelSerializer):

    class Meta:
        model =Customer
        fields ="__all__"

class GetAddressSerializers(serializers.ModelSerializer):
    
    class Meta:
        model =CustomerAddress
        fields  ="__all__"


class CustomerDetailsAddress(serializers.ModelSerializer):
    customer_address = GetAddressSerializers(many = True)

    class Meta:
        model = Customer
        fields = ('first_name,last_name,mobile,age,dob')