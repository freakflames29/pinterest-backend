from rest_framework.serializers import  ModelSerializer
from  django.contrib.auth.models import User
from board.serializers import BoardSerializer

class UserSerializer(ModelSerializer):
    boards = BoardSerializer(many=True)
    class Meta:
        model = User
        fields = ["id,","username","email","boards"]

