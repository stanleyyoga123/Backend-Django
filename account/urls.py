from .views import ListUser
from rest_framework import routers
from django.urls import path, include

router = routers.DefaultRouter()
router.register('users', ListUser)

urlpatterns = [
    path('', include(router.urls)),
]
