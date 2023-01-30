from django.db import models
#from apps.meetings.models import Meeting
#from phonenumber_field.modelfields import PhoneNumberField
    
class Contact(models.Model):
    first_name = models.CharField(max_length=200, blank=False, null=False)
    last_name = models.CharField(max_length=200, blank=False, null=False)
    email = models.EmailField(blank=False, null=False, unique=True)
    #phone_number = PhoneNumberField(blank=True)
    #phone_number = PhoneNumberField()
    phone_number = models.CharField(max_length=15, blank=True)     
    #meetings = models.ForeignKey(Meeting, on_delete=models.RESTRICT)
    
    def __str__(self):
        return f'{self.first_name} - {self.last_name}'