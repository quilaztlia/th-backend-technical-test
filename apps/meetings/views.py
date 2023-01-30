from django.shortcuts import render
from django.http import HttpResponse
from apps.meetings.models import Meeting

def meetings_list(request):
    meetings = Meeting.objects.all()
    return render(request, 'meetings/meetings_list.html', {'meetings': meetings})    
