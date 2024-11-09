from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import UserProfileViewSet, SkillViewSet, SessionViewSet, MatchViewSet

router = DefaultRouter()
router.register(r'users', UserProfileViewSet)
router.register(r'skills', SkillViewSet)
router.register(r'sessions', SessionViewSet)
router.register(r'matches', MatchViewSet)

urlpatterns = [
    path('', include(router.urls)),
]
