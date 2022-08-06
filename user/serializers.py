from rest_framework import serializers

from .models import CustomUser, AdminUpload

class UploadSerializer(serializers.ModelSerializer):

    class Meta:
        model = AdminUpload
        fields = "__all__"

class CustomUserSerializer(serializers.ModelSerializer):
    user_profile = UploadSerializer()

    class Meta:
        model = CustomUser
        fields = ("email", "name","admin_upload", "created_at", "updated_at")