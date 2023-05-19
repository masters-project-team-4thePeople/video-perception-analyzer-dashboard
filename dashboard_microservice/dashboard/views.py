import json
from random import randrange

from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from django.contrib import messages
from django.http import JsonResponse
import requests


def sign_in_page(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        users = requests.get('http://165.22.179.123/videos-api/dashboard_users/')
        users = users.json()
        for oneuser in users.values():
            print(oneuser)
            print(oneuser['username'])
            if oneuser['username'] == username:
                return redirect('apiscall')
        messages.info(request, 'Username or password is incorrect')
    context = {}
    return render(request, 'pages/sign_in.html', context)


def sign_out_page(request):
    logout(request)
    return redirect('login')


def apis_call(request):
    userCount = total_users(request)
    videoCount = video_count(request)
    user_list = user_details(request)
    video_list = video_details(request)
    video_category_likedislike = video_category_like_dislike(request)
    category_wiseCount = video_category_wiseCount(request)
    context = {
        'userCount': userCount,
        'videoCount': videoCount,
        'users': user_list,
        'videos': video_list,
        'videoCategoryTotalLike': video_category_likedislike,
        'videoCategoryCount': category_wiseCount
    }
    return render(request, 'pages/admin_dashboard.html', context)


def user_details(request):
    response = requests.get('http://165.22.179.123/videos-api/dashboard_users/')
    if response.status_code == 200:
        users = response.json()
        user_list = []
        for oneuser in users.values():
            categories = []
            for k in oneuser['categories']:
                categories.append(k)
            user_list.append({
                'username': oneuser['username'],
                'email': oneuser['email'],
                'birth_date': oneuser['birth_date'],
                'categories': categories
            })
        context = {
            'users': user_list
        }
        return user_list
        # return render(request, "pages/admin_dashboard.html", context)
    else:
        return JsonResponse({'error': 'Unable to retrieve data from API.'})


def video_details(request):
    response = requests.get('http://165.22.179.123/videos-api/dashboard_videos/')
    if response.status_code == 200:
        video_detail = response.json()
        video_list = []

        for video in video_detail.values():
            if video['video_category'] is not None:
                key, value = next(iter(video['video_category'].items()))
                video_list.append({
                    'title': video['video_title'],
                    'duration': video['video_duration'],
                    'category': value,
                    'likes': randrange(1, 5 + 1),
                    'dislikes': randrange(1, 5 + 1),
                    'url': video['video_url']
                })
        context = {
            'videos': video_list
        }
        return video_list
        # return render(request, "pages/video-details.html", context)
    else:
        return JsonResponse({'error': 'Unable to retrieve data from API.'})


# @login_required
def video_category_wiseCount(request):
    response = requests.get('http://165.22.179.123/videos-api/dashboard_videos/')
    if response.status_code == 200:
        video_detail = response.json()
        category_count = {}
        category_set = set()
        for key in video_detail:
            category_key = video_detail[key]["video_category"]
            if category_key is not None:
                key, value = next(iter(category_key.items()))
                category_count[value] = category_count.get(value, 0) + 1
        category_count_list = []
        for category, count in category_count.items():
            category_count_list.append({
                'category': category,
                'count': count
            })
        context = {
            'videoCategoryCount': category_count_list
        }
        return category_count_list
        # return render(request, "pages/video-category-count.html", context)


# @login_required
def video_category_like_dislike(request):
    response = requests.get('http://165.22.179.123/videos-api/dashboard_videos/')
    if response.status_code == 200:
        video_detail = response.json()
        category_like_count = {}
        category_dislike_count = {}

        for key in video_detail:
            category_key = video_detail[key]["video_category"]
            if category_key is not None:
                key_, value_ = next(iter(category_key.items()))
                category_like_count[value_] = category_like_count.get(value_, 0) + video_detail[key]['likes']
                category_dislike_count[value_] = category_dislike_count.get(value_, 0) + video_detail[key][
                    'dislikes']
        category_like_dislike_count = []
        for category, count in category_like_count.items():
            category_like_dislike_count.append({
                'category': category,
                'like': randrange(15, 23 + 1),
                'dislike': randrange(10, 13 + 1)
            })
        print(category_like_dislike_count)
        context = {
            'videoCategoryTotalLike': category_like_dislike_count
        }
        return category_like_dislike_count
        # return render(request, "pages/video-like-dislike.html", context)


# @login_required
def video_count(request):
    response = requests.get('http://165.22.179.123/videos-api/dashboard_videos/')
    if response.status_code == 200:
        video_detail = response.json()
        videoCount = len(video_detail)
        context = {
            'videoCount': videoCount
        }
        return videoCount
        # return render(request, "pages/dashboard.html", context)


# @login_required
def total_users(request):
    response = requests.get('http://165.22.179.123/videos-api/dashboard_users/')
    if response.status_code == 200:
        users = response.json()
        userCount = len(users)
        # print(userCount)
        context = {
            'userCount': userCount
        }
        return userCount
        # return render(request, "pages/admin_dashboard.html", context)
