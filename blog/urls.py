from django.urls import path

from blog.views import CommentAPIView, PostDetailAPIView, PostAPIView, CategoryAPIView

urlpatterns = [
    path('categories/', CategoryAPIView.as_view(), name='categories-list'),
    path('posts/', PostAPIView.as_view(), name='list-posts'),
    path('posts/<int:pk>/', PostDetailAPIView.as_view(), name='api-posts'),
    path('comments/create/', CommentAPIView.as_view(), name='comments')
]
