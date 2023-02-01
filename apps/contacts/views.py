from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status, permissions
from django.contrib.auth.models import User
from .models import Contact
from .serializers import UserSerializer, ContactSerializer

from rest_framework import viewsets
class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all().order_by('-date_joined')
    serializer_class = UserSerializer
    permissions_classes = [permissions.IsAuthenticated]    

class ContactListApiView(APIView):
    permissions_classes = [permissions.IsAuthenticated]

    def contacts_list(request):
        contacts = Contact.objects.all()
        return render(request, 'contacts/contacts_list.html', {'contacts': contacts})    

    def get(self, request, *args, **kwargs):
            #contacts = Contact.objects.filter(user=request.user.id)
            contacts = Contact.objects.all()
            serializers = ContactSerializer(contacts, many=True)
            return Response(serializers.data, status=status.HTTP_200_OK)

    def post(self, request, *args, **kwargs):
        data = {        
            'email' : request.data.get('email'),
            'first_name' : request.data.get('first_name'),
            'last_name' : request.data.get('last_name'),
            'phone_number' : request.data.get('phone_number')
        }
        serializers = ContactSerializer(data=data)
        if serializers.is_valid():
            serializers.save()
            return Response(serializers.data, status=status.HTTP_201_CREATED)
        return Response(serializers.data, status=status.HTTP_400_BAD_REQUEST)

class ContactDetailApiView(APIView):
    permissions_classes = [permissions.IsAuthenticated]

    def get_object(self, contact_id, user_id):
        try:
            return Contact.objects.get(id=contact_id)           
        except Contact.DoesNotExist:
            return None 
        
    def get(self, request, contact_id, *args, **kwargs):
        contact = self.get_object(contact_id, request.user.id) 
        if not contact:
            return Response({"res": "This contact does not exists"},   status=status.HTTP_400_BAD_REQUEST)       
        
        serializers = ContactSerializer(contact, many=False)
        return Response(serializers.data, status=status.HTTP_200_OK)    

    def put(self, request, contact_id, *args, **kwargs):
        contact = self.get_object(contact_id, request.user.id)
        if not contact:
            return Response({"res": "This contact does not exists"},   status=status.HTTP_400_BAD_REQUEST)       
        
        data = {
            'email' : request.data.get('email'),
            'first_name' : request.data.get('first_name'),
            'last_name' : request.data.get('last_name'),
            'phone_number' : request.data.get('phone_number')
        }   
        serializers = ContactSerializer(instance=contact, data=data, partial=True)
        
        if serializers.is_valid():
            serializers.save()
            return Response(serializers.data, status=status.HTTP_200_OK)

        return Response(serializers.data, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, contact_id, *args, **kwargs):
        contact = self.get_object(contact_id, request.user.id)
        if not contact:
            return Response({"res": "This contact does not exists"},   status=status.HTTP_400_BAD_REQUEST)       
        
        contact.delete()
        return Response(status=status.HTTP_200_OK)
        
