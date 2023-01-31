from django.db import models
#from phonenumber_field.modelfields import PhoneNumberField #https://django.fun/en/qa/107946/

class Contact(models.Model):   
    email = models.EmailField(blank=False, null=False, unique=True)
    first_name = models.CharField(max_length=200, blank=False, null=False)
    last_name = models.CharField(max_length=200, blank=False, null=False)         
    #phone_number = PhoneNumberField()
    phone_number = models.CharField(max_length=50, blank=True)     
    
    def __str__(self):
        return f'{self.email} : {self.first_name} - {self.last_name}'