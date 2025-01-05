from rest_framework.serializers import ModelSerializer
from .models import AccountInfo

class AccountInfoSerializer(ModelSerializer):
    class Meta:
        model = AccountInfo
        fields = "__all__"
        read_only_fields = ["user"]
