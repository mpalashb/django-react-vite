from rest_framework.serializers import ModelSerializer
from django.contrib.auth.models import User


class UserMeSerilaizer(ModelSerializer):
    class Meta:
        model = User
        fields = (
            "pk",
            "username",
            "email",
        )
