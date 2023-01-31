from django.urls import path
from rest_framework import routers
from .views import ContactListApiView

#router = routers.DefaultRouter()
#router.register(r'users', views.UserViewSet)
#routers.register(r'groups', views.)

urlpatterns = [    
    path('api', ContactListApiView.as_view())
    #path('contacts/<uuid:pk>', include(contacts_urls)),
]