from django.test import TestCase

from instapp.models import Images, Profile

# Create your tests here.

def ImageTestClass(TestCase):
    def setUp(self):
        self.new_image = Images(image_name='test image', image_caption='test caption', image_url='https://www.google.com/', image_likes=0, image_comments='test comment')
    
    def test_instance(self):
        self.assertTrue(isinstance(self.new_image, Images))
    
    def test_save_image(self):
        self.new_image.save_image()
        images = Images.objects.all()
        self.assertTrue(len(images) > 0)

def ProfileTestClass(TestCase):
    def setUp(self):
        self.new_profile = Profile(profile_name='test profile', profile_bio='test bio', profile_image='https://www.google.com/')
    
    def test_instance(self):
        self.assertTrue(isinstance(self.new_profile, Profile))
    
    def test_save_profile(self):
        self.new_profile.save_profile()
        profiles = Profile.objects.all()
        self.assertTrue(len(profiles) > 0)