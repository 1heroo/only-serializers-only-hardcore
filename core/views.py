import json

from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView


class UserInfoAPIView(APIView):

    def get(self, request):
        data = {
                'username':     f'{request.user.username}',
                'is_anonymous': f'{request.user.is_anonymous}',
                'is_staff':     f'{request.user.is_staff}',
                'is_superuser': f'{request.user.is_superuser}',
                'is_active':    f'{request.user.is_active}'
        }
        return Response(data, status=status.HTTP_200_OK)


class RequestInfoAPIView(APIView):

    def get(self, request):
        data = {
                'scheme': f'{request.scheme}',
                'path':   f'{request.path}',
                'method': f'{request.method}',
                'GET':    f'{request.GET}',
                'user':   f'{request.user}'
        }
        return Response(data, status=status.HTTP_200_OK)
