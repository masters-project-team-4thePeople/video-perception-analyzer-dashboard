from django.urls import path
from . import views

urlpatterns = [
    path('', views.sign_in_page, name='sign_in'),
]
