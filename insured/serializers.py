from rest_framework import serializers
from .models import InsurerModel
from core.models import User
from djoser.serializers import UserSerializer


class InsurerSerializer(serializers.ModelSerializer):
    email = serializers.EmailField(source='user.email', read_only=True)
    username = serializers.CharField(source='user.username', read_only=True)

    class Meta:
        fields = ['id', 'phone', 'address', 'email', 'username']
        model = InsurerModel

    def create(self, validated_data):
        user_id = self.context["user_id"]
        user = User.objects.get(id=user_id)
        return InsurerModel.objects.create(user=user, **validated_data)
