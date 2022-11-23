from rest_framework import serializers
from main.models import Inventory

class IventorySerializer(serializers.ModelSerializer):
    class Meta:
        model =Inventory
        field = '__all__'

# Create your models here.
