from django.urls import path
from .views import UserInfoAPIView, RequestInfoAPIView


urlpatterns = [
    path('request-info/', RequestInfoAPIView.as_view(), name='request-info'),
    path('user-info/', UserInfoAPIView.as_view(), name='user-info)'),
]
