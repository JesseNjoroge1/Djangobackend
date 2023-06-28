from rest_framework.serializers import ModelSerializer
from .models import AppUser

class UserSerializer(ModelSerializer):
  class Meta:
    model = AppUser
    fields = ('email', 'last_login', 'data_joined', 'is_staff')