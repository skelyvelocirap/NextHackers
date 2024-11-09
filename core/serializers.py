from rest_framework import serializers
from .models import UserProfile, Skill, UserSkill, Match, Session, Message, Notification, VolunteerHour, Feedback

class SkillSerializer(serializers.ModelSerializer):
    class Meta:
        model = Skill
        fields = ['id', 'name']

class UserSkillSerializer(serializers.ModelSerializer):
    skill = SkillSerializer(many=False)

    class Meta:
        model = UserSkill
        fields = ['id', 'user', 'skill', 'skill_type']

class MatchSerializer(serializers.ModelSerializer):
    class Meta:
        model = Match
        fields = ['id', 'mentor', 'learner', 'skill', 'status']

class UserProfileSerializer(serializers.ModelSerializer):
    skills_to_teach = SkillSerializer(many=True)
    skills_to_learn = SkillSerializer(many=True)

    class Meta:
        model = UserProfile
        fields = ['id', 'user', 'skills_to_teach', 'skills_to_learn', 'volunteer_hours']

class SessionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Session
        #fields = ['id', 'mentor', 'mentee', 'date', 'duration']
        fields = ['id', 'mentor', 'learner', 'skill', 'date', 'topic', 'status']

class MessageSerializer(serializers.ModelSerializer):
    class Meta:
        model = Message
        fields = ['id', 'session', 'sender', 'reciever', 'content', 'timestamp']

class NotificationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Notification
        fields = ['id', 'user', 'message', 'is_read', 'timestamp']

class VolunteerHourSerializer(serializers.ModelSerializer):
    class Meta:
        model = VolunteerHour
        fields = ['id', 'mentor', 'hours', 'session', 'date']

class FeedbackSerializer(serializers.ModelSerializer):
    class Meta:
        model = Feedback
        fields = ['id', 'session', 'rating', 'comments']

class MatchSerializer(serializers.ModelSerializer):
    class Meta:
        model = Match
        fields = '__all__'