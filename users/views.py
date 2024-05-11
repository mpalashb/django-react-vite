from django.shortcuts import render
from django.views import View
from django.views.generic import (
    TemplateView
)


class UserHomePage(View):
    def get(self, request, *args, **kwargs):
        return render(request, template_name="user_home.html")


class UserDashboard(TemplateView):
    template_name = "dashboard.html"
