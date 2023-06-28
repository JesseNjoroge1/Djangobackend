from django.contrib.auth import get_user_model, login, logout
from rest_framework.authentication import TokenAuthentication
from rest_framework.views import APIView
from rest_framework.response import Response
from .serializers import UserRegisterSerializer, UserLoginSerializer, UserSerializer
from rest_framework import permissions, status
from rest_framework.decorators import api_view, permission_classes


class UserRegister(APIView):
  permission_classes = (permissions.AllowAny)
  def post(self, request):
    data = request.data
    serializer = UserRegisterSerializer(data)
    if serializer.is_valid(raise_exception=True):
      user = serializer.create(data)
      if user:
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    return Response(status=status.HTTP_400_BAD_REQUEST)

class UserLogin(APIView):
  permission_classes = (permissions.AllowAny,)
  authentication_class = (TokenAuthentication,)

  def post(self, request):
    data = request.data
    serializer = UserLoginSerializer(data=data)
    if serializer.is_valid(raise_exception=True):
      user = serializer.check_user(data)
      login(request, user)
      return Response(serializer.data, status=status.HTTP_200_OK)
class UserLogout(APIView):
  def post(self, request):
    logout(request)
    return Response(status=status.HTTP_200_OK)


@api_view(['GET', 'POST'])
@permission_classes([permissions.IsAuthenticated])
class UserView(APIView):
  authentication_classes = (TokenAuthentication,)

  def get(self, request):
    serializer = UserSerializer(request.user)
    return Response({'user': serializer.data}, status=status.HTTP_200_OK)