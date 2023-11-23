from django.contrib import admin
from django.urls import path, include

from rest_framework_simplejwt import views as jwt_view

from . import views

urlpatterns = [
    path('register/', views.RegiterUserView.as_view()),
    path('login/', views.LoginUserView.as_view()),
    path('profile/', views.ProfileUserView.as_view()),
    path('password/change/', views.ChangePasswordView.as_view()),
    path('token/', jwt_view.TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('token/refresh/', jwt_view.TokenRefreshView.as_view(), name='token_refresh'),
]