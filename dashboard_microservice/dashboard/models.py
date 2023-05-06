from django.db import models

# from django.contrib.auth.models import AbstractUser
from django.contrib.auth.models import User


class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    birth_date = models.DateField(null=True, blank=True)
    notification_id = models.CharField(max_length=256, blank=True)


class UserPreference(models.Model):
    user_id = models.ForeignKey(UserProfile, on_delete=models.CASCADE, blank=True, null=False)
    user_categories = models.JSONField(blank=True, null=True)
    user_video_history = models.JSONField(blank=True, null=True)


class VideoMetaData(models.Model):
    video_id = models.BigAutoField(primary_key=True)
    video_url = models.CharField(max_length=512, default='', blank=True, null=True)
    video_title = models.CharField(max_length=256, default='', blank=True, null=True)
    video_duration = models.FloatField(default=0.0, blank=True, null=True)
    video_likes = models.IntegerField(default=0, blank=True, null=True)
    video_dislikes = models.IntegerField(default=0, blank=True, null=True)
    video_transcription = models.CharField(max_length=2048, default='', blank=True, null=True)
    video_category = models.JSONField(blank=True, null=True)
    video_information = models.JSONField(blank=True, null=True)


class VideoDetails(models.Model):
    user_id = models.ForeignKey(UserProfile, on_delete=models.CASCADE, blank=True, null=True)
    video_id = models.ForeignKey(VideoMetaData, on_delete=models.CASCADE, blank=True, null=True)
