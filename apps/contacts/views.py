from django.shortcuts import render
from django.http import HttpResponse
from .models import Contact

def contacts_list(request):
    contacts = Contact.objects.all()
    return render(request, 'contacts/contacts_list.html', {'contacts': contacts})
