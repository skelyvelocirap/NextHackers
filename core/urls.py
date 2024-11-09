from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import UserProfileViewSet, SkillViewSet, SessionViewSet, FeedbackViewSet

router = DefaultRouter()
router.register(r'users', UserProfileViewSet)
router.register(r'skills', SkillViewSet)
router.register(r'sessions', SessionViewSet)
router.register(r'feedback', FeedbackViewSet)

urlpatterns = [
    path('', include(router.urls)),
]