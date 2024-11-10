from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import UserProfileViewSet, SkillViewSet, UserSkillViewSet, SessionViewSet, MessageViewSet, NotificationViewSet, VolunteerHourViewSet, FeedbackViewSet, MatchViewSet

router = DefaultRouter()
router.register(r'users', UserProfileViewSet)
router.register(r'skills', SkillViewSet)
router.register(r'sessions', SessionViewSet)
router.register(r'matches', MatchViewSet)
router.register(r'user_skills', UserSkillViewSet)
router.register(r'message', MessageViewSet)
router.register(r'notification', NotificationViewSet)
router.register(r'volunteer_hour', VolunteerHourViewSet)
router.register(r'feedback', FeedbackViewSet)

urlpatterns = [
    path('', include(router.urls)),
]