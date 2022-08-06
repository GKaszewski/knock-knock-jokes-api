from django.urls import path, include
from rest_framework import routers
from .views import JokeViewSet

router = routers.DefaultRouter()
router.register('', JokeViewSet)

urlpatterns = [
    path('', include(router.urls))
]