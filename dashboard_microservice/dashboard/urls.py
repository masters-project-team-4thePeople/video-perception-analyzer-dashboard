from django.urls import path
from . import views
from django.contrib.auth import views as auth_views


urlpatterns = [
    path('login/', views.sign_in_page, name='login'),
    path('logout', views.sign_out_page, name='logout'),
    path('users', views.user_details, name='user-Profile'),
    path('videoCategoryCount', views.video_category_wiseCount, name='video-Category-Count'),
    path('videoCategoryList', views.video_category_like_dislike, name='video-Category-likes-dislike'),
    path('videoCount', views.video_count, name='video-count'),
    path('userCount', views.total_users, name='users-count'),
    path('videos', views.video_details, name='video-information'),
]
