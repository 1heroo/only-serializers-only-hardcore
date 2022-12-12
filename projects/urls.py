from django.urls import path
from .views import ProjectsDetailAPIView, ProjectsAPIView

urlpatterns = [
    path('projects/', ProjectsAPIView.as_view(), name='projects-list'),
    path('projects/<int:pk>/', ProjectsDetailAPIView.as_view(), name='api-projects')
]
