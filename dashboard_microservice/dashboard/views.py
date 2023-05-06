from django.shortcuts import render, redirect
from django.http import JsonResponse
from dashboard.models import UserProfile, VideoMetaData
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login, logout
from dashboard.serializers import UserDetailsSerializer
from django.contrib.auth.models import User
from django.db.models import Count
from django.db.models import Sum
from django.contrib import messages
from dashboard.models import VideoDetails


def sign_in_page(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = User.objects.filter(username=username, password=password).first()
        if user is not None:
            context = {}
            return render(request, 'pages/total-users-card.html', context)
        else:
            messages.info(request, 'Username or password is incorrect')

    context = {}
    return render(request, 'pages/sign_in.html', context)


def sign_out_page(request):
    logout(request)
    context = {}
    return render(request, 'pages/sign_in.html', context)

@login_required
# user details
def user_details(request):
    if request.method == 'GET':
        usersInfo = User.objects.all()
        print(usersInfo)
        context = {
            'usersInfo': usersInfo
        }
        return render(request, "pages/user-details.html", context)

@login_required
# category wise video count
def video_category_wiseCount(request):
    if request.method == 'GET':
        # videoInfo = VideoDetails.objects.all()
        videoCategoryCount = VideoDetails.objects.values('video_category').annotate(count=Count('video_category'))
        context = {
            'videoCategoryCount': videoCategoryCount
        }
        print(context)
        return render(request, "pages/video-category-count.html", context)

@login_required
# # video category and like/dislike
def video_category_like_dislike(request):
    if request.method == 'GET':
        grouped_data = VideoMetaData.objects.values('video_category').annotate(totalLike=Sum('video_likes'),
                                                                               totalDisLike=Sum(
                                                                                   'video_dislikes')).order_by(
            'video_category')
        print(grouped_data)
        # {'video_Category': , 'totalLike': , 'totalDisLike': }
        context = {
            'videoCategoryTotalLike': grouped_data
        }
        return render(request, "pages/video-like-dislike.html", context)


@login_required
def video_count(request):
    if request.method == 'GET':
        videoInfo = VideoDetails.objects.count()
        print(videoInfo)
        context = {
            'videoCount': videoInfo
        }
        print(context)
        return render(request, "pages/total-videos-card.html", context)

@login_required
def total_users(request):
    if request.method == 'GET':
        userCount = User.objects.count()
        print(userCount)
        context = {
            'userCount': userCount
        }
        print(context)
        return render(request, "pages/total-users-card.html", context)
