from django.urls import path, include
from .views import RegisterAPIView, ResetPasswordAPIView, ResetPasswordCompleteAPIView, PasswordTokenVerifyAPIView, \
    ChangePasswordAPIView

urlpatterns = [
    # register
    path('auth/register/', RegisterAPIView.as_view(), name='register-api'),

    # reset user's password
    path('auth/reset-password-complete/', ResetPasswordCompleteAPIView.as_view(), name='reset-password-complete'),
    path('auth/reset-password/', ResetPasswordAPIView.as_view(), name='reset-password'),
    path('auth/reset-token-verify/<uidb64>/<token>/', PasswordTokenVerifyAPIView.as_view(), name='reset-token-verify'),

    # change password
    path('auth/change-password/', ChangePasswordAPIView.as_view(), name='change-passwrd'),
]

urlpatterns += [
    path('api/login/', include('rest_social_auth.urls_token')),
]
