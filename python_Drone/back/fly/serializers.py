from rest_framework import serializers
from .models import FlySaying

class FlySayingSerializer(serializers.ModelSerializer) :
    class Meta:
        model = FlySaying
        fields = '__all__'