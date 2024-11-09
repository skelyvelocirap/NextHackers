from django.db import models
from django.contrib.auth.models import User

class Skill(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name

class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    skills_to_teach = models.ManyToManyField(Skill, related_name='mentors')
    skills_to_learn = models.ManyToManyField(Skill, related_name='learners')
    volunteer_hours = models.IntegerField(default=0)

class Session(models.Model):
    mentor = models.ForeignKey(UserProfile, related_name='mentor_sessions', on_delete=models.CASCADE)
    mentee = models.ForeignKey(UserProfile, related_name='mentee_sessions', on_delete=models.CASCADE)
    date = models.DateTimeField()
    duration = models.IntegerField(help_text="Duration in minutes")

class Feedback(models.Model):
    session = models.ForeignKey(Session, on_delete=models.CASCADE)
    rating = models.IntegerField()
    comment = models.TextField(blank=True)