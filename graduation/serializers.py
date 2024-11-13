from .models import *
from rest_framework import serializers

class RegistrationSerializer(serializers.ModelSerializer):
    class Meta():
        model = NewAdmission
        fields = '__all__'

    
