from rest_framework import viewsets
from account.models import CustomUser
from account.serializers import UserSerializer
from rest_framework import permissions


class UserViewSet(viewsets.ModelViewSet):
    queryset = CustomUser.objects.all()
    serializer_class = UserSerializer
    permission_classes = [permissions.AllowAny]
