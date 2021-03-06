from rest_framework import viewsets
from rest_framework.authentication import TokenAuthentication
from rest_framework import filters
from rest_framework.authtoken.views import ObtainAuthToken
from rest_framework.settings import api_settings
from rest_framework.permissions import IsAuthenticated

from .models import UserProfile, ProfileFeedItem
from .serializers import UserProfileSerializer, ProfileFeedItemSerializer
from .permissions import UpdateOwnProfile, UpdateOwnFeed


class UserProfileViewSet(viewsets.ModelViewSet):
    """Handle creating and updating Profiles"""
    queryset = UserProfile.objects.all()
    serializer_class = UserProfileSerializer
    authentication_classes = (TokenAuthentication,)
    permission_classes = (UpdateOwnProfile,)
    filter_backends = (filters.SearchFilter,)
    search_fields = ('name', 'email',)


class UserLoginApiView(ObtainAuthToken):
    """Handles creating user authentication tokens"""
    renderer_classes = api_settings.DEFAULT_RENDERER_CLASSES


class ProfileFeedItemViewSet(viewsets.ModelViewSet):
    """Handles creating, reading, updating and deleting feed items"""
    authentication_classes = (TokenAuthentication,)
    serializer_class = ProfileFeedItemSerializer
    queryset = ProfileFeedItem.objects.all()
    permission_classes = [UpdateOwnFeed, IsAuthenticated]

    def perform_create(self, serializer):
        serializer.save(user_profile=self.request.user)
