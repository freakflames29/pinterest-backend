from rest_framework.serializers import  ModelSerializer,SerializerMethodField
from .models import Comment

class CommentSerializer(ModelSerializer):
    username = SerializerMethodField(read_only=True)
    profile_img = SerializerMethodField(read_only=True)

    def get_username(self,obj):
        return  obj.user.username
    
    def get_profile_img(self,obj):
        try:
            print("+"*100,obj.user.info.profile_img)
            request = self.context.get("request")
            if obj.user.info.profile_img:
                return request.build_absolute_uri(obj.user.info.profile_img.url)
        except:
            return "#"


    class Meta:
        model= Comment
        fields = ["id","pin","body","username","profile_img"]
        read_only_fields = ["pin"]
