from django.db import models

# Create your models here.
class Images(models.Model):
    image_name = models.CharField(max_length=100)
    image_caption = models.CharField(max_length=10000)
    image_url = models.ImageField(upload_to='instagram/')
    image_likes = models.IntegerField(default=0)
    image_comments = models.TextField( blank=True)

    def __str__(self):
        return self.image_name
    
    def save_image(self):
        self.save()

    def delete_image(self):
        self.delete()
    
    def update_caption(self, new_caption):
        self.image_caption = new_caption
        self.save()
