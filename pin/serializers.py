from rest_framework.serializers import ModelSerializer,SerializerMethodField
from .models import Pin


class PinSerializer(ModelSerializer):
    username= SerializerMethodField(read_only=True)
    
    def get_username(self,obj):
        return obj.user.username
    
    class Meta:
        model = Pin
        fields = ["id","title","link","desc","image","user","username","boards"]
        read_only_fields = ["user"]
