from django.db import models
from django.contrib.auth.models import User


class AccountInfo(models.Model):
    gender_choice = (("M","Male"),("F","Female"),)
    user = models.OneToOneField(User,on_delete=models.CASCADE,related_name="info")
    profile_img = models.ImageField(upload_to="profile/image/",blank=True)
    gender = models.CharField(max_length=2,choices=gender_choice,blank=True)
    desc   = models.TextField(blank=True)
    
    def __str__(self):
        return self.desc
    
    
    