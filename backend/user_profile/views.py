from django.shortcuts import render
from rest_framework.views import APIView
from user_profile.models import UserActions, Page, Action
from users.models import User
from trip_planning.models import Item
from user_profile.serializers import UserActionSerializer, EventSerializer
from rest_framework.response import Response
from rest_framework.viewsets import ReadOnlyModelViewSet, ModelViewSet
from bson import ObjectId, json_util
from rest_framework import status
from rest_framework.decorators import action
from django.shortcuts import get_object_or_404
import json




# Create your views here.

class UserActionView(ModelViewSet):
    serializer_class = EventSerializer
    
    @action(detail=False, methods=['post'])
    def save_user_action_view(self, request):
        try:
            user = request.user
            item = request.item
            event_type = request.data.get("eventType")
            event_data = request.data.get("data")

            # Debugging prints
            print(f"User: {user}")
            print(f"User: {item}")
            print(f"Event Type: {event_type}")
            print(f"Event Data: {event_data}")

            data = {
                "user": user.id,  
                "item": item.id,  
                "event_type": event_type,
                "data": event_data
            }

            print(f"Data: {data}")

            event_serializer = self.serializer_class(data=data)
            if event_serializer.is_valid():
                event_serializer.save()
                data = event_serializer.data
                print(data)
                event = {
                    "id": data['id'],
                    "user": User.objects.get(pk=data['user']).username,
                    "item": Item.objects.get(pk=data['item']).name,
                    "event_type": data['event_type'],
                    "data": data['data'],
                    "timestamp": data['timestamp']
                } 
                
                return Response(data=event, status=status.HTTP_201_CREATED)
            else:
                print(f"Validation Errors: {event_serializer.errors}")
                return Response(data=event_serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        except Exception as e:
            print(f"Exception: {e}")
            return Response({"error": str(e)}, status=status.HTTP_400_BAD_REQUEST)

    # @action(detail=False, methods=['post'])
    # def save_user_action_view(self, request):
    #     try:
    #         user_id = request.data.get("user")
    #         action_id = request.data.get("action")

    #         # Debugging prints
    #         print(f"User ID: {user_id}")
    #         print(f"Action ID: {action_id}")

    #          # Check if the objects exist in the database
    #         user = get_object_or_404(User, _id=ObjectId(user_id))
    #         action = get_object_or_404(Action, _id=ObjectId(action_id))

    #         data = {
    #             "user": ObjectId(user._id),  
    #             "action": ObjectId(action._id) 
    #         }

    #         print(f"Data: {data}")

    #         useraction_serializer = self.serializer_class(data=data)
    #         if useraction_serializer.is_valid():
    #             useraction_serializer.save()
    #             data = useraction_serializer.data
    #             print(data)
    #             useraction = {
    #                 "id": data['_id'],
    #                 "user": User.objects.get(pk=data['user']).first_name,
    #                 "action": Action.objects.get(pk=data['action']).name
    #             } 
                
    #             useraction = json.loads(json_util.dumps(useraction))

    #             return Response(data=useraction, status=status.HTTP_201_CREATED)
    #         else:
    #             print(f"Validation Errors: {useraction_serializer.errors}")
    #             return Response(data=useraction_serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    #     except Exception as e:
    #         print(f"Exception: {e}")
    #         return Response({"error": str(e)}, status=status.HTTP_400_BAD_REQUEST)


