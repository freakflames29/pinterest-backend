from rest_framework.serializers import ModelSerializer, SerializerMethodField
from .models import Pin


class PinSerializer(ModelSerializer):
    username = SerializerMethodField(read_only=True)
    user_image =  SerializerMethodField(read_only=True)
    # photo_url = SerializerMethodField(read_only=True)
    
    
   

    def get_username(self, obj):
        return obj.user.username

    def get_photo_url(self, obj):
        rq = self.context.get("request")
        print(rq,"8"*100)
        if rq:

            photo_url = obj.image.url
            return rq.build_absolute_uri(photo_url)
        else:
            return "#"
    
    def get_user_image(self,obj):
        try:
            if obj.user.info:
              rq = self.context.get("request")
              if rq:
                  url = obj.user.info.profile_img.url
                #   return url
                  return rq.build_absolute_uri(url)
                
               
        except:
            return "#"

    class Meta:
        model = Pin
        fields = ["id", "title", "link", "desc",
                  "user", "username", "image","user_image"]
        read_only_fields = ["user"]
