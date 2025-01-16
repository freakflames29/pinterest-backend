from django.db import models

class Category(models.Model):
    title = models.CharField(max_length=100)
    banner = models.ImageField(upload_to="banner/",blank=True)
    
    def __str__(self):
        return self.title
    
    