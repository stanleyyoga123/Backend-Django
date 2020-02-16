from .views import ListOrder
from rest_framework import routers
from django.urls import path, include

router = routers.DefaultRouter()
router.register('order', ListOrder)

urlpatterns = [
	path('', include(router.urls)),
]