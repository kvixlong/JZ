from django.contrib import admin

from Insta.models import InstaUser, Post, Comment, Like

# Register your models here.
admin.site.register(InstaUser)
admin.site.register(Post)
admin.site.register(Like)
admin.site.register(Comment)

