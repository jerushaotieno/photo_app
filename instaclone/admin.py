from django.contrib import admin
from .models import Image, Profile, Comments, FollowUser

# Register your models here.

admin.site.register(Image)
admin.site.register(Profile)
admin.site.register(Comments)
admin.site.register(FollowUser) 