from rest_framework.serializers import ModelSerializer,SerializerMethodField
from .models import AccountInfo



# {
# 	"id": 4,
# 	"profile_img": "http://127.0.0.1:8000/media/profile/image/__1_xCESj4N.jpeg",
# 	"gender": "M",
# 	"desc": "change from logic v2",
# 	"user": 9
# }
class AccountInfoSerializer(ModelSerializer):
    username = SerializerMethodField(read_only=True)
    
    def get_username(self,obj):
        return obj.user.username
    
    class Meta:
        model = AccountInfo
        fields = ["id","profile_img","gender","desc","username","user"]
        read_only_fields = ["user"]
