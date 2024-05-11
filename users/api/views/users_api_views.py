from rest_framework import permissions, response, status
from rest_framework.generics import views, GenericAPIView
from ..serializers.users_serializers import (
    UserMeSerilaizer
)


class UserMeAPI(GenericAPIView):
    permission_classes = (
        permissions.IsAuthenticated,
    )

    def get(self, request, *args, **kwargs):
        serializeView = UserMeSerilaizer(request.user)
        return response.Response(
            data=serializeView.data,
            status=status.HTTP_200_OK
        )
