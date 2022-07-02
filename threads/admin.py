from django.contrib import admin

from .models import Thread, Comment, Upvote

admin.site.register(Thread)
admin.site.register(Comment)
admin.site.register(Upvote)
