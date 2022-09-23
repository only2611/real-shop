

from rest_framework.routers import DefaultRouter
from django.urls import path, include

from api_v1.views import ProductViewSet, OrderViewSet

app_name = "api_v1"


router = DefaultRouter()
router.register("products", ProductViewSet)
router.register("orders", OrderViewSet)

urlpatterns = [
    path('', include(router.urls))
]
