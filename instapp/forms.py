from django import forms
from models import Insta_Images

class NewInstaImages(forms.ModelForm):
     class Meta:
        model = Insta_Images
        exclude = ['image_likes']
        

