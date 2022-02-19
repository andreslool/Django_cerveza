from rest_framework import serializers
from .models import chela

class chelaserializer(serializers.ModelSerializer):
    class Meta:
        model = chela
        fields = '__all__'
        