
from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('properties/', views.properties, name='properties'),
    path('property/<int:prop_id>', views.property_detail, name='property_detail'),
]