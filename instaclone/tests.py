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
        self.test_user = User(user_name='Jay', password='code')
        self.test_user.save()

        self.test_user_profile = User.objects.last().user_profile
        self.test_user_profile.save()        

        self.test_comment = Comments(user_name=self.test_user_profile, comment_details='sample comment', commented_on=datetime.now())
        self.test_comment.save()

        self.test_image = Image(image='images/test.jpg', image_caption='sample text', profile_foreign_key=self.test_profile_profile_key, image_comments=self.test_image_comments, published_on=datetime.now())

    def test_instance(self):
        '''
        ensures image instance is created
        '''
        self.assertTrue(isinstance(self.test_image, Image))

    def tearDown(self):
        ''' '''
        self.test_user.delete()
        Profile.objects.all().delete()
        Comments.objects.all().delete()
        Image.objects.all().delete() 

    def test_save(self):
        '''
        saves instance to db
        '''
        self.test_image.save_image()
        self.assertEqual(len(Image.objects.all()), 1)


# Profile Model Tests

class ProfileTest(TestCase):
    '''
    test class for Profile model
    '''
    def setUp(self):
        '''
        method called before each test
        '''
        self.user = User.objects.create_user(user_name='Dino')

    def tearDown(self):
        '''
        method clears all setup instances after running each test
        '''
        self.user.delete()

    def test_user_profile_creation(self):
        '''
        tests that profile instance is created only once for eavery user
        '''
        self.assertIsInstance(self.user.user_profile, Profile)
        self.user.save()
        self.assertIsInstance(self.user.user_profile, Profile)