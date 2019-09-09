from rest_framework import serializers

from .models import UserProfile


class UserProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserProfile
        fields = ['id', 'email', 'name', 'password']
        extra_kwargs = {
            'password': {
                'write_only': True,
                'style': {'input_type': 'password'}
            }
        }

    def create(self, validated_data):
        user = UserProfile.objects.create_user(
            email=self.validated_data['email'],
            name=self.validated_data['name'],
            password=self.validated_data['password']
        )

        return user
