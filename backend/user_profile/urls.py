from django.urls import path, include
from rest_framework import routers
from user_profile.views import UserActionView


router = routers.DefaultRouter()
router.register(r'useractions', UserActionView, 'useraction')

urlpatterns = [
    path('', include(router.urls)),
]
