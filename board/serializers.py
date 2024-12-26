from rest_framework.serializers import ModelSerializer, SerializerMethodField
from .models import Board
from pin.serializers import PinSerializer

class BoardSerializer(ModelSerializer):
    user_name = SerializerMethodField(read_only=True)
    pins =PinSerializer(read_only=True,many=True)

    def get_user_name(self, obj):
        return obj.user.username
    
    # def get_pins(self,obj):
    #     pins = obj.pins.all()
    #     return PinSerializer(pins,many=True,context=self.context).data

    class Meta:
        model = Board
        fields = ["id", "name", "user", "user_name","pins"]
        read_only_fields = ["user"]
