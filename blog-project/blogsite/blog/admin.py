from django.contrib import admin
from blog.models import Comment, Post, User

# Register your models here.
admin.site.register(Post)
admin.site.register(Comment)
admin.site.register(User)
