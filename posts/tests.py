from django.test import TestCase
from django.contrib.auth.models import User
from .models import Project,UserProfile

# Create your tests here.
class ProfileTestClass(TestCase):
    def setUp(self):
        '''
        Set Up method to run before each test case
        '''
        self.new_user = User.objects.create_user(username='user',password='user-password')
        self.new_profile = UserProfile(id=1,user=self.new_user,profile_pic='photos/pic',bio='user-bio')

    def test_instance(self):
        self.assertTrue(isinstance(self.new_profile,UserProfile))


    def test_save_profile(self):
        self.new_profile.save_profile()
        profiles = UserProfile.objects.all()
        self.assertTrue(len(profiles) > 0)