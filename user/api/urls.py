from django.contrib import admin
from django.urls import path, include

from . import views

urlpatterns = [
    path('register/', views.RegiterUserView.as_view()),
    path('login/', views.LoginUserView.as_view()),
    path('profile/', views.ProfileUserView.as_view()),
]