from django.urls import path

from todo_app.views import ListListAPIView, ListDetailAPIView, ListItemAPIView, ItemDetailAPIView


urlpatterns = [
    path('', ListListAPIView.as_view(), name='list-lists'),
    path('list/<int:pk>/', ListDetailAPIView.as_view(), name='api-lists'),

    path('create/item/', ListItemAPIView.as_view(), name='create-item'),
    path('item/<int:pk>/', ItemDetailAPIView.as_view(), name='api-item')
]