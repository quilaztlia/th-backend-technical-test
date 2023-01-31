from django.urls import path
from rest_framework import routers
from .views import ContactListApiView, ContactDetailApiView

#router = routers.DefaultRouter()
#router.register(r'users', views.UserViewSet)
#routers.register(r'groups', views.)

urlpatterns = [    
    path('api', ContactListApiView.as_view()),
    path('api/<int:contact_id>', ContactDetailApiView.as_view())
]