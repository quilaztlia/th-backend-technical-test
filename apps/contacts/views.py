#from django.shortcuts import render
#from django.http import HttpResponse
from django.contrib.auth.models import User
from rest_framework import viewsets
from rest_framework import permissions
from .serializers import UserSerializer, ContactSerializer
from .models import Contact

# def contacts_list(request):
#     contacts = Contact.objects.all()
#     return render(request, 'contacts/contacts_list.html', {'contacts': contacts})

class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all().order_by('-date_joined')
    serializer_class = UserSerializer
    permissions_classes = [permissions.IsAuthenticated]    