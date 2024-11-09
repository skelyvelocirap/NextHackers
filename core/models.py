from django.db import models
from django.contrib.auth.models import User

def __str__(self):
    return self.name

class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    role = models.CharField(max_length=10, choices=[('mentor', 'Mentor'), ('learner', 'Learner'), ('both', 'Both')])
    bio = models.TextField(blank=True)
    profile_pic = models.CharField(max_length=255, blank=True)
    volunteer_hours = models.FloatField(default=0.0)

class Skill(models.Model):
    name = models.CharField(max_length=50, unique=True)

class UserSkill(models.Model):
    user = models.ForeignKey(UserProfile, on_delete=models.CASCADE)
    skill = models.ForeignKey(Skill, on_delete=models.CASCADE)
    skill_type = models.CharField(max_length=10, choices=[('teach', 'Teach'), ('learn', 'Learn')])

class Match(models.Model):
    mentor = models.ForeignKey(UserProfile, related_name="mentor_matches", on_delete=models.CASCADE)
    learner = models.ForeignKey(UserProfile, related_name="learner_matches", on_delete=models.CASCADE)
    skill = models.ForeignKey(Skill, on_delete=models.CASCADE)
    status = models.CharField(max_length=10, choices=[('pending', 'Pending'), ('accepted', 'Accepted'), ('declined', 'Declined')])

class Session(models.Model):
    mentor = models.ForeignKey(UserProfile, related_name="mentor_sessions", on_delete=models.CASCADE)
    learner = models.ForeignKey(UserProfile, related_name="learner_sessions", on_delete=models.CASCADE)
    skill = models.ForeignKey(Skill, on_delete=models.CASCADE)
    date = models.DateTimeField()
    topic = models.CharField(max_length=255)
    status = models.CharField(max_length=10, choices=[('scheduled', 'Scheduled'), ('completed', 'Completed'), ('canceled', 'Canceled')])

class Message(models.Model):
    session = models.ForeignKey(Session, on_delete=models.CASCADE)
    sender = models.ForeignKey(UserProfile, related_name="sent_messages", on_delete=models.CASCADE)
    receiver = models.ForeignKey(UserProfile, related_name="received_messages", on_delete=models.CASCADE)
    content = models.TextField()
    timestamp = models.DateTimeField(auto_now_add=True)

class Notification(models.Model):
    user = models.ForeignKey(UserProfile, on_delete=models.CASCADE)
    message = models.TextField()
    is_read = models.BooleanField(default=False)
    timestamp = models.DateTimeField(auto_now_add=True)

class VolunteerHour(models.Model):
    mentor = models.ForeignKey(UserProfile, on_delete=models.CASCADE)
    session = models.ForeignKey(Session, on_delete=models.CASCADE)
    hours = models.FloatField()
    date = models.DateField()

class Feedback(models.Model):
    session = models.ForeignKey(Session, on_delete=models.CASCADE)
    reviewer = models.ForeignKey(UserProfile, on_delete=models.CASCADE)
    rating = models.IntegerField()
    comment = models.TextField(blank=True)
    timestamp = models.DateTimeField(auto_now_add=True)





