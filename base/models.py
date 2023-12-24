from django.db import models
from django.contrib.auth.models import User

class Topic(models.Model):
    name = models.CharField(max_length=200)

    def __str__(self):
        return self.name
    

class Room(models.Model):
    host = models.ForeignKey(User,on_delete=models.SET_NULL, null=True)
    topic = models.ForeignKey(Topic,on_delete=models.SET_NULL, null=True)
    name = models.CharField(max_length=200)
    description = models.TextField(null=True, blank=True)  # null=True => it can't be blank (for data base) --- blank=True => that form can be empty(for save method when adding a form)
    # participants = 
    updated = models.DateTimeField(auto_now=True) # here => take a snapchat on every time we save this item here
    created = models.DateTimeField(auto_now_add=True)# here => only takes the time when we first save or create this instance
    # the id set by default

    class Meta:
        ordering = ['-updated','-created']

    def __str__(self):
        return self.name

    
class Message(models.Model):
    user = models.ForeignKey(User,on_delete=models.CASCADE)
    room = models.ForeignKey(Room, on_delete=models.CASCADE) # if the parent will be delete(Room) same for all the children 
    body = models.TextField()
    updated = models.DateTimeField(auto_now=True)
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.body[0:50]
    
