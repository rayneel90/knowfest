from rest_framework import serializers
from .models import SignInput, SignOutput

class SignInputSerializer(serializers.ModelSerializer):
    class Meta:
        model = SignInput
        fields = [
            'source',
            'cust_id',
            'image',
        ]
