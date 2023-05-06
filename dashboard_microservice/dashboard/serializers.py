from rest_framework import serializers
from dashboard.models import UserDetails, UserPreference, VideoDetails


class UserDetailsSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserDetails
        fields = (
            'user_id',
            'first_name',
            'last_name',
            'email_address',
            'date_of_birth',
            'notification_id'
        )


class UserPreferencesSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserPreference
        fields = (
            'user_id',
            'user_categories',
            'user_video_history'
        )


class VideoDetailsSerializer(serializers.ModelSerializer):
    class Meta:
        model = VideoDetails
        fields = (
            'user_id',
            'video_id',
            'video_title',
            'video_duration',
            'video_views',
            'video_likes',
            'video_dislikes'
        )
