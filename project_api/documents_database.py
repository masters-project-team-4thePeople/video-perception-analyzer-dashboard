from mongoengine import Document, StringField, ListField, EmailField, \
    DateField, DictField, FloatField, IntField, URLField, UUIDField


# User DetailsDocument Class
class UserDetails(Document):
    user_id = UUIDField(required=True, binary=False)
    first_name = StringField(required=True)
    last_name = StringField(required=True)
    password = StringField(required=True)
    email_address = EmailField(required=True)
    date_of_birth = DateField(required=True)
    notification_id = StringField()
    meta = {'allow_inheritance': True}


# User Preferences Document Class
class UserPreferences(Document):
    user_id = UUIDField(required=True, binary=False)
    user_categories = ListField()
    user_video_history = DictField()
    meta = {'allow_inheritance': True}


# Video Details Document Class
class VideoDetails(Document):
    user_id = UUIDField(required=True, binary=False)
    video_id = UUIDField(required=True, binary=False)
    video_title = StringField(required=True)
    video_duration = FloatField(required=True)
    video_views = IntField(required=True)
    video_likes = IntField(required=True)
    video_dislikes = IntField(required=True)
    meta = {'allow_inheritance': True}


# Video MetaData Document Class
class VideoMetadata(Document):
    video_id = UUIDField(required=True, binary=False)
    video_url = URLField(required=True)
    video_title = StringField(required=True)
    video_duration = FloatField(required=True)
    video_views = FloatField(required=True)
    video_likes = IntField(required=True)
    video_dislikes = IntField(required=True)
    video_category = ListField()
    video_transcription = DictField()
    video_information = DictField()
    meta = {'allow_inheritance': True}
