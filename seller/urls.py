from django.urls import path, include
from . import views

urlpatterns = [
    path('get_contact_info/', views.get_contact_info, name='get_contact'),
]