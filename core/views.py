from django.shortcuts import render

# Create your views here.
from rest_framework import viewsets
from .models import UserProfile, Skill, UserSkill, Match, Session, Message, Notification, VolunteerHour, Feedback
from .serializers import UserProfileSerializer, SkillSerializer, UserSkillSerializer, MatchSerializer, SessionSerializer, MessageSerializer, NotificationSerializer, VolunteerHourSerializer, FeedbackSerializer
from .models import UserProfile, Skill, Session, Feedback, Match
from .serializers import UserProfileSerializer, SkillSerializer, SessionSerializer, FeedbackSerializer, MatchSerializer

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


class MatchView(APIView):
    def get(self, request, user_id):
        # Fetch skills the user wants to learn
        user_skills = UserSkill.objects.filter(user_id=user_id, skill_type='learn')
        skills_to_learn = [user_skill.skill_id for user_skill in user_skills]

        # Find mentors who can teach those skills
        matches = UserSkill.objects.filter(skill_id__in=skills_to_learn, skill_type='teach').select_related('user')

        # Format the results as a JSON response
        matched_mentors = [
            {
                "mentor_id": match.user.id,
                "mentor_name": match.user.user.username,  # Assuming username is in User model
                "skill": match.skill.name,
            }
            for match in matches
        ]

        return Response({"matches": matched_mentors})