from logins.serializer import *
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView
from tools_rest.response_view import success
from tools_rest.swagger_view import SwaggerResultViewModel
from rest_framework.generics import CreateAPIView
from rest_framework.permissions import AllowAny
from drf_yasg.utils import swagger_auto_schema

class GenerateTokenView(TokenObtainPairView):
    serializer_class = GenerateTokenSerializer
    
    @swagger_auto_schema(responses={200: SwaggerResultViewModel(TokenReponseSerializer).openapi}, tags=['login'])
    def post(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        return success(serializer.validated_data)

class GenerateTokenRefreshView(TokenRefreshView):
    @swagger_auto_schema(responses={200: SwaggerResultViewModel(TokenReponseSerializer).openapi}, tags=['login'])
    def post(self, request, *args, **kwargs):
        return super().post(request, *args, **kwargs)
    
class RegisterUserView(CreateAPIView):
    queryset = CustomUser.objects.all()
    permission_classes = (AllowAny,)
    serializer_class = RegisterSerializer
    
    @swagger_auto_schema(responses={200: SwaggerResultViewModel(ResponseRegisterSerializer).openapi}, tags=['login'])
    def post(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        instance = serializer.save()
        serializer_response = ResponseRegisterSerializer(instance)
        return success(serializer_response.data)