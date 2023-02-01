from django.db import models
from django.conf import settings
from django.utils import timezone
from apps.contacts.models import Contact
#from django.contrib.auth.models import User

#30min : magic String! => Constants
class Meeting(models.Model):
    #TODO: delete?
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)     

    TODO = 'Todo'
    CANC = 'Canceled'
    ONGO = 'Ongoing'
    COMP = 'Completed'    
    MEETING_STATUS_CHOICES = [
        (TODO, 'Todo'),
        (CANC, 'Canceled'),
        (ONGO, 'Ongoing'),
        (COMP, 'Completed'),
    ]
    
    title = models.CharField(max_length=200, blank=False, null=False, unique=True) 
    description = models.TextField(blank=True, null=False, default='') 
    datetime = models.DateTimeField(blank=False, null=False, default=timezone.now())
    duration = models.DurationField(blank=False, null=False, default=30) 
    status = models.CharField(max_length=9, choices= MEETING_STATUS_CHOICES, default=TODO)
    contacts = models.ManyToManyField(Contact, None)

    def __str__(self):
        return f'{self.title} at {self.datetime}'