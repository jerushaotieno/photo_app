from django.test import TestCase
from .models import Image, Profile, Comments, FollowUser
from datetime import datetime
from django.contrib.auth.models import User

# Create your tests here.

# Image Model Tests

class TestImage(TestCase):
    def setUp(self):
        '''
        creates image instances called before each test case
        '''
        self.test_user = User(username='Jay', password='code')
        self.test_user.save()
        self.test_profile = Profile(user=self.test_user, photo='avatars/anime.jpg')

        self.test_comment = Comments(name=self.test_profile, comment_details='Sample comment', commented_on=datetime.now())

        self.test_image = Image(image='images/test.jpg', image_caption='sample text', profile=self.test_profile, comments=self.test_comment, created_on=datetime.now())

    def test_instance(self):
        ''' '''
        self.assertTrue(isinstance(self.test_image, Image))

    def tearDown(self):
        ''' '''
        self.test_user.delete()
        Profile.objects.all().delete()
        Comments.objects.all().delete()
        Image.objects.all().delete() 