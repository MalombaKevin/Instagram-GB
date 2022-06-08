from django.urls import path
from . import views
from django.conf.urls.static import static
from django.conf import settings


urlpatterns = [
    path('', views.index, name='index'),
    path('post', views.insta_post,name='newPost' ),
    path('update', views.newPost,name='post' ),
    path('profile', views.profile,name='profile' ),
    path('updateProfile', views.update_profile,name='newProfile' ),
]

if settings.DEBUG:
    urlpatterns+= static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)