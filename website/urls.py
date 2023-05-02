from django.urls import path, include
from . import views


urlpatterns = [
     path('',views.home, name='home'),
     path('web1',views.web1, name='web1'),
     path('web2',views.web2, name='web2'),
     path('web3',views.web3, name='web3'),
     path('web4',views.web4, name='web4'),
]
