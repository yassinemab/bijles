from django.urls import path

from bijles_backend.views import AvailabilityView, ProfilesView

from .views import AuthView, RequestsView, MatchesView, LocationsView, ApplicationsView, ReviewsView, SubjectsView

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
    path('getApplicationsByRequestId',
         ApplicationsView.getApplicationsByRequestId),
    path('deleteApplication', ApplicationsView.deleteApplication),
    path('handleMatch', MatchesView.handleMatch),
    path('getOwnMatches', MatchesView.getOwnMatches),
    path('getIncomingMatches', MatchesView.getIncomingMatches),
    path('getOutgoingMatches', MatchesView.getOutgoingMatches),
    path('getAllLocations', LocationsView.getAllLocations),
    path('insertReview', ReviewsView.insertReview),
    path('getReviewsByUserId', ReviewsView.getReviewsByUserId),
    path('getOwnReviews', ReviewsView.getOwnReviews),
    path('deleteReview', ReviewsView.deleteReview),
    path('changeProfile', ProfilesView.changeProfile),
    path('addSubjectToUser', SubjectsView.addSubjectToUser),
    path('deleteSubjectFromUser', SubjectsView.deleteSubjectFromUser),
    path('getAllAvailabilities', AvailabilityView.getAllAvailabilities),
    path('addAvailabilityToUser', AvailabilityView.addAvailabilityToUser),
    path('deleteAvailabilityFromUser', AvailabilityView.deleteAvailabilityFromUser),
]
