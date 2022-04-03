from django.db import models

# Create your models here.

# Image Model

class Image(models.Model):
    image = models.ImageField(upload_to='images/')
    image_name = models.CharField(max_length=30)
    image_caption = models.TextField()
    profile_foreign_key = models.ForeignKey('Profile', on_delete=models.CASCADE)


#  Profile Model

class Profile(models.Model):
    profile_photo = models.ImageField(upload_to='avatars/')
    profile_bio = models.TextField() 
