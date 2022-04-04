from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework.exceptions import PermissionDenied
from ..models import Users
from ..models.Requests import Requests as RequestsModel
from ..models.Subjects import Subjects as SubjectsModel
from ..models.Applications import Applications as ApplicationsModel
from ..models.Matches import Matches as MatchesModel
from ..models.Roles import Roles as RolesModel
from ..models.Reviews import Reviews as ReviewsModel
from ..models.MatchStatusses import MatchStatusses as MatchStatusModel
from ..models.RequestStatusses import RequestStatusses as RequestStatusModel
from ..serializers import ApplicationsSerializer, RequestsSerializer, ReviewsSerializer, SubjectsSerializer
from . import UsersView, MatchesView


@api_view(["POST"])
def insertReview(request):
    title = request.data["title"]
    if len(title) > 100:
        raise PermissionDenied("Title is too long")

    content = request.data["content"]
    if len(content) > 500:
        raise PermissionDenied("Content is too long")

    rating = request.data["rating"]
    if not rating:
        rating = 1

    student = UsersView.getUser(request._request)
    student_role = RolesModel.objects.filter(name="Student").first()
    if student.data["role_id"] != student_role.id:
        raise PermissionDenied("The user writing the review must be a student")

    teacher = Users.objects.filter(id=request.data["teacher_id"]).first()
    teacher_role = RolesModel.objects.filter(name="Teacher").first()
    if not teacher or teacher.role_id != teacher_role.id:
        raise PermissionDenied("Teacher is invalid")

    if teacher.id == student.data["id"]:
        raise PermissionDenied("Cannot place review on self")

    match_status = MatchStatusModel.objects.filter(name="Accepted").first()
    match_exists = MatchesModel.objects.filter(initiator_id=student.data["id"], target_id=request.data["teacher_id"], match_status=match_status).exists(
    ) or MatchesModel.objects.filter(target_id=student.data["id"], initiator_id=request.data["teacher_id"], match_status=match_status).exists()
    if not match_exists:
        raise PermissionDenied(
            "There must be a match between the target and the iniator")

    review_exists = ReviewsModel.objects.filter(
        student_id=student.data["id"], teacher=teacher).exists()
    if review_exists:
        raise PermissionDenied("Review is already placed")

    review = ReviewsModel.objects.create(
        content=content, title=title, student_id=student.data["id"], teacher=teacher, rating=rating)
    review.save()
    return Response({"message": True})


# Only for teachers
@api_view(["GET"])
def getReviewsByUserId(request):
    user = Users.objects.filter(id=request.GET["id"]).first()
    teacher_role = RolesModel.objects.filter(name="Teacher").first()
    if not user or user.role_id != teacher_role.id:
        raise PermissionDenied("User not found")

    reviews = ReviewsModel.objects.filter(teacher=user)
    serializer = ReviewsSerializer(reviews, many=True)
    return Response(serializer.data)


# Only for students
@api_view(["GET"])
def getOwnReviews(request):
    user = UsersView.getUser(request._request)
    student_role = RolesModel.objects.filter(name="Student").first()
    if user.data["role_id"] != student_role.id:
        raise PermissionDenied("User is not a student")
    reviews = ReviewsModel.objects.filter(student_id=user.data["id"])
    serializer = ReviewsSerializer(reviews, many=True)
    return Response(serializer.data)

@api_view(["DELETE"])
def deleteReview(request):
    user = UsersView.getUser(request._request)
    review = ReviewsModel.objects.filter(id=request.data["id"]).first()
    if not review:
        raise PermissionDenied("Review not found")
    if review.student_id != user.data["id"]:
        raise PermissionDenied("Review is written by the user")
    review.delete()
    return Response({"message": True})
