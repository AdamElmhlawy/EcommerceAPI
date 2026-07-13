from django.contrib.auth import get_user_model
User = get_user_model()

from rest_framework import serializers

class RegisterSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True)

    class Meta:
        model = User
        fields = ('username', 'email', 'phone_number', 'password')

    def create(self, validated_data):
        user = User.objects.create_user(**validated_data)
        return user