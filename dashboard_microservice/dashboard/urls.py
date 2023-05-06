from django.urls import path
from . import views

urlpatterns = [
    path('', views.sign_in_page, name='sign_in'),
    path('users', views.user_details, name='user Profile'),
    path('videoCategoryCount', views.video_category_wiseCount, name='video Category Count'),
    path('videoCategoryList', views.video_category_like, name='video Category likes'),
    path('videoCategoryDislike', views.video_category_dislike, name='video Category Dislike'),
]
