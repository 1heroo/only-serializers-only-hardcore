from rest_framework import status
from rest_framework.response import Response

from .models import Project
from rest_framework.views import APIView

from .serializers import ProjectSerializer


class ProjectsAPIView(APIView):

    def get(self, request):
        projects = Project.objects.all()
        return Response(projects.values_list(), status=status.HTTP_200_OK)


class ProjectsDetailAPIView(APIView):

    def get_object(self, pk):
        return Project.objects.get(pk=pk)

    def get(self, request, pk):
        serializer = ProjectSerializer(self.get_object(pk=pk))
        return Response(serializer.data, status=status.HTTP_200_OK)
