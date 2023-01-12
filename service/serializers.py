from rest_framework import serializers
from rest_framework.exceptions import PermissionDenied

from .models import Taxi, Order


class TaxiSerializer(serializers.ModelSerializer):

    class Meta:
        model = Taxi
        fields = '__all__'
        read_only_fields = ['profile']


class OrderSerializer(serializers.ModelSerializer):

    class Meta:
        model = Order
        fields = '__all__'
