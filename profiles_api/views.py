from django.shortcuts import render
from rest_framework import viewsets
from rest_framework.authentication import TokenAuthentication

from .models import UserProfile
from .serializers import UserProfileSerializer
from .permissions import UpdateOwnProfile


class UserProfileViewSet(viewsets.ModelViewSet):
    """Handle creating and updating Profiles"""
    queryset = UserProfile.objects.all()
    serializer_class = UserProfileSerializer
    authentication_classes = (TokenAuthentication,)
    permission_classes = (UpdateOwnProfile,)
