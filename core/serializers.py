from rest_framework import serializers
from .models import UserProfile, Skill, Session, Feedback

class SkillSerializer(serializers.ModelSerializer):
    class Meta:
        model = Skill
        fields = ['id', 'name']

class UserProfileSerializer(serializers.ModelSerializer):
    skills_to_teach = SkillSerializer(many=True)
    skills_to_learn = SkillSerializer(many=True)

    class Meta:
        model = UserProfile
        fields = ['id', 'user', 'skills_to_teach', 'skills_to_learn', 'volunteer_hours']

class SessionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Session
        fields = ['id', 'mentor', 'mentee', 'date', 'duration']

class FeedbackSerializer(serializers.ModelSerializer):
    class Meta:
        model = Feedback
        fields = ['id', 'session', 'rating', 'comments']