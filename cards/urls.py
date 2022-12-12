from django.urls import path
from cards.views import CardAPIView, CardDetailAPIView, BoxAPIView


urlpatterns = [
    path('cards/', CardAPIView.as_view(), name='card-list'),
    path('cards/<int:pk>/', CardDetailAPIView.as_view(), name='api-cards'),
    path('box/<int:box_id>/', BoxAPIView.as_view(), name='api-box')
]

