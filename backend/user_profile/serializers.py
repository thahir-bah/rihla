from rest_framework.serializers import ModelSerializer
from user_profile.models import *

class UserActionSerializer(ModelSerializer):
    class Meta:
        model = UserActions
        fields = '__all__'

class EventSerializer(ModelSerializer):
    class Meta:
        model = Event
        fields = '__all__'