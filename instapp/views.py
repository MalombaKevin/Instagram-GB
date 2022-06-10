from multiprocessing import context
from django.shortcuts import redirect, render
from django.contrib.auth.decorators import login_required
from instapp.forms import NewInstaImages, NewInstaProfile
from instapp.models import Images, Profile
from django.contrib.auth.models import User



# Create your views here.
# @login_required(login_url='/accounts/login/')
def index(request):
    
    current_user = request.user
    images = Images.objects.all()
    all_users = User.objects.all()

    try:
        user = User.objects.get(username = current_user.username)
        users = User.objects.exclude(username=current_user.username).exclude(is_superuser=True)
    except:
        user = None
        users = None
    
    return render(request, 'index.html', {"images": images, "user": user, "users": users, "all_users": all_users})


@login_required(login_url='/accounts/login/')
def newPost(request):
    return render(request, 'post.html')

@login_required(login_url='/accounts/login/')
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

@login_required(login_url='/accounts/login/')
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

@login_required
def profile(request):
    user = User.objects.get(username=request.user.username)
    images = Images.objects.all()
    return render(request, 'profile.html', {"images": images, "user": user, "profile": profile})

@login_required
def search_results(request):
    if 'search' in request.GET and request.GET['search']:
        search_term = request.GET.get('search')
        images = Images.search_image(search_term)
        message = f'{search_term}'
            
        return render(request, 'search.html', { "images": images, "message": message})

    else:
        message = "You haven't searched for any term"
    return render(request, 'search.html', {"message": message})


 

    
