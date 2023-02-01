from django.urls import path
from .views import MeetingListApiView, MeetingDetailApiView

urlpatterns = [
   path('api', MeetingListApiView.as_view()),
   path('api/<int:meeting_id>', MeetingDetailApiView.as_view())
]