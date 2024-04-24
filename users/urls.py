from users.apps import UsersConfig
from django.urls import path

from users.views import UserAuthAPIView, UserVerificationAPIView

app_name = UsersConfig.name

urlpatterns = [
    path('get_code/', UserAuthAPIView.as_view(), name='get_code'),
    path('verify_code/', UserVerificationAPIView.as_view(), name='verify_code'),
]
