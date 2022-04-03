from django.db import models
from django.contrib.auth.models import User

# Create your models here.

# Image Model

class Image(models.Model):
    image = models.ImageField(upload_to='images/')
    image_name = models.CharField(max_length=30)
    image_caption = models.TextField()
    profile_foreign_key = models.ForeignKey('Profile', on_delete=models.CASCADE)
    image_likes = models.ManyToManyField(User, blank=True)
    image_comments = models.ForeignKey('Comments', on_delete=models.CASCADE)
    published_on = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['?'] #order randomly on feed

    def __str__(self):
        return self.image_name

    def save_image(self):
        '''
        method saves image
        '''
        self.save()

    def delete_image(self):
        '''
        method deletes image
        '''
        self.delete()

    def update_caption(self, new_caption):
        ''' 
        method updates image caption 
        '''
        self.image_caption = new_caption
        self.save()

    @classmethod    
    def get_user_images(cls, user_id):
        ''' 
        method retrieves all images
        '''
        all_images = Image.objects.filter(profile=user_id).all()
        sort = sorted(all_images, key=lambda t: t.created_on)
        return sort


#  Profile Model

class Profile(models.Model):
    profile_photo = models.ImageField(upload_to='avatars/')
    profile_bio = models.TextField() 
