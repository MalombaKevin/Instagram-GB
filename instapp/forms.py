from django import forms
from .models import Images

class NewInstaImages(forms.ModelForm):
     class Meta:
        model = Images
        fields = '__all__'
        exclude = ['image_likes']
        

