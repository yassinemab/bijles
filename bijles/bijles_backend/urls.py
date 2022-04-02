from django.urls import path
from . import views

urlpatterns = [
    path('', views.getAllUsers),
    path('add/', views.addUser)
]
