from django.urls import path
from . import views

urlpatterns = [
    path('', views.showUsers, name='showUsers'),
]
