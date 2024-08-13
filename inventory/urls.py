from django.urls import include, path
from rest_framework import routers
from inventory import views


router = routers.DefaultRouter()

router.register('', views.InventoryItemViewSet, basename='inventory')

urlpatterns = [
    path('', include(router.urls)),
]
