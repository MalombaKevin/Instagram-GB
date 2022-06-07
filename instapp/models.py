from django.db import models

# Create your models here.
class Insta_Images(models.Model):
    image_name = models.CharField(max_length=100)
    image_caption = models.CharField(max_length=10000)
    image_url = models.ImageField(upload_to='images/')
    image_likes = models.IntegerField(default=0)
    image_comments = models.IntegerField(default=0)

    def __str__(self):
        return self.image_name
