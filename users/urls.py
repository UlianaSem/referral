from users.apps import UsersConfig
from django.urls import path

from users.views import UserAuthAPIView, UserVerificationAPIView, \
    UserProfileRetrieveAPIView, UserCodeAPIView

app_name = UsersConfig.name

urlpatterns = [
    path('get_code/', UserAuthAPIView.as_view(), name='get_code'),
    path('verify_code/', UserVerificationAPIView.as_view(), name='verify_code'),

    path('profile/<int:pk>/', UserProfileRetrieveAPIView.as_view(), name='get_profile'),
    path('add_invite_code/<int:pk>/', UserCodeAPIView.as_view(), name='add_invite_code'),
]
