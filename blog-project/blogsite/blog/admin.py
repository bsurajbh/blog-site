from django.contrib import admin
from django.contrib.admin import ModelAdmin

from blog.models import Comment, Post, User, Category


class PostAdmin(ModelAdmin):
    model = Post
    list_display = ('title', 'author', 'published_date',)
    ordering = ('-create_date',)


admin.site.register(Post, PostAdmin)
admin.site.register(Comment)
admin.site.register(User)
admin.site.register(Category)
