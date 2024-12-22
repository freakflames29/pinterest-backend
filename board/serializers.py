from rest_framework.serializers import ModelSerializer, SerializerMethodField
from .models import Board


class BoardSerializer(ModelSerializer):
    user_name = SerializerMethodField(read_only=True)

    def get_user_name(self, obj):
        return obj.user.username

    class Meta:
        model = Board
        fields = ["id", "name", "user", "user_name"]
        read_only_fields = ["user"]
