from django.shortcuts import redirect, render

from instapp.forms import NewInstaImages, NewInstaProfile
from instapp.models import Images, Profile

# Create your views here.
def index(request):
    images= Images.objects.all()
    return render(request, 'index.html', {"images": images})

def newPost(request):
    return render(request, 'post.html')

def insta_post(request):
    if request.method == 'POST':
        form = NewInstaImages(request.POST, request.FILES)
        if form.is_valid():
            instapost= form.save()
            instapost.save()
        return redirect ('index')
    else:
        form=NewInstaImages()
    
    return render (request, 'forms/new_post.html', {"form": form})

def update_profile(request):
    if request.method == 'POST':
        form = NewInstaProfile(request.POST, request.FILES)
        if form.is_valid():
            instaprofile= form.save()
            instaprofile.save()
        return redirect ('profile')
    else:
        form=NewInstaProfile()  

    return render(request, 'forms/addprofile.html', {"form": form})

def profile(request):
    profile = Profile.objects.all()
    images = Images.objects.all()
    return render(request, 'profile.html', {"images": images, "profile": profile})



    
