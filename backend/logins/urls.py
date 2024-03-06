from django.urls import path
from logins.views import GenerateTokenView, RegisterUserView, GenerateTokenRefreshView

urlpatterns = [
    path('', GenerateTokenView.as_view(), name='token_obtain_pair'),
    path('refresh/', GenerateTokenRefreshView.as_view(), name='token_refresh'),
    path('register/', RegisterUserView.as_view(), name='auth_register')
]
