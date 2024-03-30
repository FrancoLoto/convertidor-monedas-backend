from rest_framework import serializers
from .models import Currency


# Serializer for the Currency model
class CurrencySerializer(serializers.ModelSerializer):
    class Meta:
        model = Currency
        fields = ['code']
