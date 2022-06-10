from django.db import models

# Create your models here.
class Profile(models.Model):
    profile_name = models.CharField(max_length=100)
    profile_bio = models.CharField(max_length=10000, blank=True)
    profile_image = models.ImageField(upload_to='profile/')
   
    def __str__(self):
        return self.profile_name
    
    def save_profile(self):
        self.save()

    def delete_profile(self):
        self.delete()
    
    def update_bio(self, new_bio):
        self.profile_bio = new_bio
        self.save()


class Images(models.Model):
    image_name = models.CharField(max_length=100)
    image_caption = models.CharField(max_length=10000)
    image_url = models.ImageField(upload_to='instagram/')
    image_likes = models.IntegerField(default=0)
    image_comments = models.TextField( blank=True)
    image_by = models.ForeignKey(Profile, on_delete=models.CASCADE, null=True, blank=True)

    def __str__(self):
        return self.image_name
    
    def save_image(self):
        self.save()

    def delete_image(self):
        self.delete()
    
    def update_caption(self, new_caption):
        self.image_caption = new_caption
        self.save()
    
    def search_image(self, search_term):
        return Images.objects.filter(image_name__icontains=search_term)

