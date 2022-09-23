from django.shortcuts import render
from rest_framework.permissions import DjangoModelPermissions, SAFE_METHODS, IsAdminUser
from rest_framework.viewsets import ModelViewSet

from api_v1.serializers import ProductModelSerializer, OrderModelSerializer
from webapp.models import Product, Order


# Create your views here.


class ProductViewSet(ModelViewSet):
    queryset = Product.objects.all()
    serializer_class = ProductModelSerializer
    permission_classes = [IsAdminUser, DjangoModelPermissions]

    def get_permissions(self):
        if self.request.method in SAFE_METHODS:
            return []
        return super().get_permissions()


class OrderViewSet(ModelViewSet):
    queryset = Order.objects.all()
    serializer_class = OrderModelSerializer
    # permission_classes = [IsAdminUser, DjangoModelPermissions]

