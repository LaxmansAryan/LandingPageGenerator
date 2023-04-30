from django.urls import path
from . import views

urlpatterns = [
     path('',views.home, name='home'),
     path('website',views.website, name='website'),
     path('website1',views.website1, name='website1'),
]
