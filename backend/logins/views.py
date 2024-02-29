from logins.serializer import *
from rest_framework_simplejwt.views import TokenObtainPairView
from tools_rest.response_view import success, bad_request
from rest_framework.generics import CreateAPIView
from rest_framework.permissions import AllowAny, IsAuthenticated
from rest_framework.exceptions import ErrorDetail

class GenerateTokenView(TokenObtainPairView):
    serializer_class = GenerateTokenSerializer
    
    def post(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        return success(serializer.validated_data)
    
class RegisterUserView(CreateAPIView):
    queryset = CustomUser.objects.all()
    permission_classes = (AllowAny,)
    serializer_class = RegisterSerializer
    
    def post(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        try:
            serializer.is_valid(raise_exception=True)
        except ParseError as error:
                return bad_request(error.args[0])
        except Exception as ex:
            return ex
        
        serializer.save()
        return success(serializer.data)