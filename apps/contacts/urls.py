from django.urls import path
from rest_framework import routers
from . import views

router = routers.DefaultRouter()
router.register(r'users', views.UserViewSet)
#routers.register(r'groups', views.)

urlpatterns = [
    #path('', views.contacts_list, name='contacts_list.html'),
    
    #TODO: path('api', ContactListApiView.as_view())
]