from django.shortcuts import render
from .models import Image, Profile, Comments, FollowUser

# Create your views here.

def user_feed(request):
    images = Image.objects.all()
    return render(request, 'index.html')


def user_profile(request):
    return render(request, 'user_profile.html') 

