#from django.conf.urls import url
from django.urls import path
#from django.urls import path, include
from .views import (
    MeetingListApiView,
)


from . import views

urlpatterns = [
   #path('', views.meetings_list, name='meetings_list.html'),
   path('api', MeetingListApiView.as_view()),
]