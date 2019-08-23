from django.contrib import admin
from blog.models import Comment, Post, User,Category

# Register your models here.
admin.site.register(Post)
admin.site.register(Comment)
admin.site.register(User)
admin.site.register(Category)
