from django.urls import path
from logins.views import GenerateTokenView, RegisterUserView

from rest_framework_simplejwt.views import (TokenRefreshView,)

urlpatterns = [
    path('', GenerateTokenView.as_view(), name='token_obtain_pair'),
    path('refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('register/', RegisterUserView.as_view(), name='auth_register')
]
