from django.urls import path
from .views import EntryDetailAPIView, EntryListAPIView


urlpatterns = [
    path('entry-list/', EntryListAPIView.as_view(), name='entry-list'),
    path('entry/<int:pk>/', EntryDetailAPIView.as_view(), name='api-entry')
]