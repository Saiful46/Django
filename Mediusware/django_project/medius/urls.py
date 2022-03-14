from django.urls import path, include
from .views import *
from . import views

urlpatterns = [
    path('', views.HomeView.as_view(), name='home'),
]
