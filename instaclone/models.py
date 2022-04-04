from django.db import models
from django.contrib.auth.models import User
from django.dispatch import receiver
from django.db.models.signals import post_save

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
        sorted_images = sorted(all_images, key=lambda t: t.published_on)
        return sorted_images


#  Profile Model

class Profile(models.Model):
    user_profile = models.OneToOneField(User, on_delete=models.CASCADE)
    profile_photo = models.ImageField(default='default.jpg', upload_to='avatars/')
    profile_bio = models.TextField(max_length=500, blank=True, default=f'Hi, I am {User.username}')

    def __str__(self):
        return f'user_profile {self.user_profile.username}'

    def save_image(self):
        ''' 
        saves a user's profile 
        '''
        self.save()

    def delete_profile(self):
        '''
        deletes a user's profile 
        '''
        self.delete()

    def update_profile_bio(self, user_profile_id, new_profile_bio):
        ''' method to update a users profile bio '''
        user_profile = User.objects.get(id=user_profile_id)
        self.profile_bio = new_profile_bio
        self.save()

    def update_image(self, user_profile_id, new_image):
        ''' method to update a users profile image '''
        user_profile = User.objects.get(id=user_profile_id)
        self.photo = new_image
        self.save()

@receiver(post_save, sender=User)
def create_user_profile(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(user_profile=instance)

@receiver(post_save, sender=User)
def save_user_profile(sender, instance, **kwargs):
    instance.user_profile.save()


# Comments Model

class Comments(models.Model):
    user_name = models.ForeignKey('Profile', on_delete=models.CASCADE)
    comment_details = models.TextField()
    commented_on = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['commented_on']

    def save_comment(self):
        ''' 
        saves a comment
        '''
        self.save()

    def delete_comment(self):
        '''
        deletes a comment
        '''
        self.delete()

    def edit_comment(self, new_comment):
        '''
        edits a comment
        '''
        self.comment_details = new_comment
        self.save()

    def __str__(self):
        return 'Comment by {self.user_name}'



# Follow User Model

class FollowUser(models.Model):
    follower = models.ForeignKey('Profile', related_name='following', on_delete=models.CASCADE)
    following = models.ForeignKey('Profile', related_name='follower', on_delete=models.CASCADE)

    class Meta:
        unique_together = ('follower', 'following')

    def __str__(self):
        return '{self.follower} follows {self.following}'
