from django.contrib import admin

from .models import FriendRequest, User

admin.site.register(FriendRequest)
admin.site.register(User)
