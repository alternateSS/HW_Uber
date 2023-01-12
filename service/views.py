
from rest_framework import viewsets
from .models import Taxi, Profile, Order

from .serializers import TaxiSerializer, OrderSerializer

from .permissions import IsProfilePermission


class TaxiViewSet(viewsets.ModelViewSet):
    queryset = Taxi.objects.all()
    serializer_class = TaxiSerializer

    def perform_create(self, serializer):
        serializer.save(profile=self.request.user.profile)


class OrderViewSet(viewsets.ModelViewSet):
    queryset = Order.objects.all()
    serializer_class = OrderSerializer
    permission_classes = [IsProfilePermission]

    def perform_create(self, serializer):
        serializer.save(profile=self.request.user.profile)

