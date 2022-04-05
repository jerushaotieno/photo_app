from django.shortcuts import render
from .models import Image, Profile, Comments, FollowUser
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required

# Create your views here.

def user_feed(request):
    images = Image.objects.all()
    return render(request, 'index.html', {'images':images})


@login_required(login_url='/accounts/login/')
def user_profile(request):
    return render(request, 'user_profile.html') 


#  Search functionality

def search(request):
    if 'category' in request.GET and request.GET['category']:
        search_for = request.GET.get('instasearch')
        result = Image.search_image(search_for)
        message = f'{search_for}'

        return render(request, 'search.html', {'message':message, 'result':result})
    else:
        message = 'Type something else to search for'
        return render(request, 'search.html', {'message':message}) 