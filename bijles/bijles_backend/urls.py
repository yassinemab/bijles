from django.urls import path
from . import views

urlpatterns = [
    path('logout', views.logout),
    path('user', views.getUser),
    path('register', views.register),
    path('login', views.login),
    path('createRequest', views.createRequest),
    path('getRequestById', views.getRequestById),
    path('getOwnRequests', views.getOwnRequests)
]
