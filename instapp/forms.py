from django import forms
from .models import Images, Profile

class NewInstaImages(forms.ModelForm):
     class Meta:
        model = Images
        fields = '__all__'
        exclude = ['image_likes']

class NewInstaProfile(forms.ModelForm):
     class Meta:
        model = Profile
        fields = '__all__'
        exclude = ['profile_image']
        

