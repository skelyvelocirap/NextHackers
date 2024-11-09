from django.shortcuts import render

# Create your views here.
from rest_framework import viewsets
from .models import UserProfile, Skill, UserSkill, Match, Session, Message, Notification, VolunteerHour, Feedback, Match
from .serializers import UserProfileSerializer, SkillSerializer, UserSkillSerializer, MatchSerializer, SessionSerializer, MessageSerializer, NotificationSerializer, VolunteerHourSerializer, FeedbackSerializer, MatchSerializer

class MatchViewSet(viewsets.ModelViewSet):
    queryset = Match.objects.all()
    serializer_class = MatchSerializer
class UserProfileViewSet(viewsets.ModelViewSet):
    queryset = UserProfile.objects.all()
    serializer_class = UserProfileSerializer


class SkillViewSet(viewsets.ModelViewSet):
    queryset = Skill.objects.all()
    serializer_class = SkillSerializer

class UserSkillViewSet(viewsets.ModelViewSet):
    queryset = UserSkill.objects.all()
    serializer_class = UserSkillSerializer

class MatchViewSet(viewsets.ModelViewSet):
    queryset = Match.objects.all()
    serializer_class = MatchSerializer

class SessionViewSet(viewsets.ModelViewSet):
    queryset = Session.objects.all()
    serializer_class = SessionSerializer

class MessageViewSet(viewsets.ModelViewSet):
    queryset = Message.objects.all()
    serializer_class = MessageSerializer

class NotificationViewSet(viewsets.ModelViewSet):
    queryset = Notification.objects.all()
    serializer_class = NotificationSerializer

class VolunteerHourViewSet(viewsets.ModelViewSet):
    queryset = VolunteerHour.objects.all()
    serializer_class = VolunteerHourSerializer
    
class FeedbackViewSet(viewsets.ModelViewSet):
    queryset = Feedback.objects.all()
    serializer_class = FeedbackSerializer