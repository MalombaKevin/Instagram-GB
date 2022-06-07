from django.shortcuts import redirect, render

from instapp.forms import NewInstaImages

# Create your views here.
def index(request):
    return render(request, 'index.html')

def insta_post(request):
    if request.method == 'POST':
        form = NewInstaImages(request.POST, request.FILES)
        if form.is_valid():
            instapost= form.save()
            instapost.save()
        return redirect ('index')
    else:
        form=NewInstaImages
    
    return render (request, 'post.html', {"form": form})

    
