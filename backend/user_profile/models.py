# from django.db import models
from djongo import models
from users.models import User
from trip_planning.models import Item
# Create your models here.

    
class Page(models.Model):
    _id = models.ObjectIdField()
    url = models.CharField(max_length=50, blank=True)
    title = models.CharField(max_length=50)
    date_created = models.DateTimeField(auto_now_add=True)
    date_updated = models.DateTimeField(auto_now=True)

class Action(models.Model):
    _id = models.ObjectIdField()
    name = models.CharField(max_length=50)
    # type = models.fields.CharField(max_length=255)
    # description = models.fields.CharField(max_length=255)
    date_created = models.DateTimeField(auto_now_add=True)
    date_updated = models.DateTimeField(auto_now=True)
    
    def __str__(self):
        return self.name
    
class UserActions(models.Model):
    _id = models.ObjectIdField()
    user = models.ForeignKey(to=User, on_delete=models.CASCADE)
    action = models.ForeignKey(to=Action, on_delete=models.CASCADE)
    timestamp = models.DateTimeField(auto_now=True)

class UserItemView(models.Model):
    _id = models.ObjectIdField()
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    item = models.ForeignKey(Item, on_delete=models.CASCADE)
    view_start = models.DateTimeField()
    view_end = models.DateTimeField()
    timestamp = models.DateTimeField(auto_now=True)

class SearchQueries(models.Model):
    _id = models.ObjectIdField()
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    query_text = models.CharField(max_length=255)
    timestamp = models.DateTimeField(auto_now=True)
    

class Event(models.Model):
    event_type = models.CharField(max_length=50)
    data = models.JSONField()
    timestamp = models.DateTimeField(auto_now_add=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    item = models.ForeignKey(Item, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.event_type} by {self.user} at {self.timestamp}"
