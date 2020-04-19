from django import forms
from blog.models import Post, Comment, User
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
import django_filters


class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ('title', 'text', 'category')

        widgets = {
            'title': forms.TextInput(
                attrs={'class': 'textinputclass form-control'}
            ),
            'text': forms.Textarea(
                attrs={'class': 'editable medium-editor-textarea postcontent form-control'}
            )
        }


class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ('author', 'text')

        widgets = {
            'author': forms.TextInput(
                attrs={'class': 'textinputclass form-control'}
            ),
            'text': forms.Textarea(
                attrs={'class': 'editable medium-editor-textarea postcontent form-control'}
            )
        }


class CustomUserCreationForm(UserCreationForm):
    class Meta(UserCreationForm):
        model = User
        fields = ('email', 'name')


class BlogFilter(django_filters.FilterSet):
    title = django_filters.CharFilter(lookup_expr='icontains')
    category = django_filters.NumberFilter(field_name='category__id', lookup_expr='iexact')

    class Meta:
        model = Post
        fields = ['title','category']
