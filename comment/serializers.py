from rest_framework.serializers import  ModelSerializer,SerializerMethodField
from .models import Comment

class CommentSerializer(ModelSerializer):
    username = SerializerMethodField(read_only=True)

    def get_username(self,obj):
        return  obj.user.username


    class Meta:
        model= Comment
        fields = ["id","pin","body","username"]
        read_only_fields = ["pin"]
