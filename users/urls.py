from django.urls import path
from .views import (
    UserHomePage,
    UserDashboard,
)

app_name = "users"

urlpatterns = [
    path('', UserHomePage.as_view(), name="user-home"),
    path('dashboard', UserDashboard.as_view(), name="user-dashboard"),
]
