from django.urls import path

from bijles_backend.views import ApplicationsView, SubjectsView
from .views import AuthView, UsersView, RequestsView, MatchesView

urlpatterns = [
    path('logout', AuthView.logout),
    path('register', AuthView.register),
    path('login', AuthView.login),
    path('changePassword', AuthView.changePassword),
    path('createRequest', RequestsView.createRequest),
    path('getRequestById', RequestsView.getRequestById),
    path('getOwnRequests', RequestsView.getOwnRequests),
    path('deleteRequest', RequestsView.deleteRequest),
    path('getAllSubjects', SubjectsView.getAllSubjects),
    path('insertApplication', ApplicationsView.insertApplication),
    path('getYourApplications', ApplicationsView.getYourApplications),
    path('getApplicationsByRequestId', ApplicationsView.getApplicationsByRequestId),
    path('deleteApplication', ApplicationsView.deleteApplication),
    path('handleMatch', MatchesView.handleMatch),
    path('getOwnMatches', MatchesView.getOwnMatches),
    path('getIncomingMatches', MatchesView.getIncomingMatches),
    path('getOutgoingMatches', MatchesView.getOutgoingMatches),
]
