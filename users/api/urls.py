from django.urls import path
from .views.users_api_views import (
    UserMeAPI
)

urlpatterns = [
    path('api/auth/me', UserMeAPI.as_view()),
]
