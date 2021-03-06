from .views import ListCollected
from rest_framework import routers
from django.urls import path, include

router = routers.DefaultRouter()
router.register('collected', ListCollected)

urlpatterns = [
	path('', include(router.urls)),
]