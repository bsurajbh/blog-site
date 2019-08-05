from django import forms
from blog.models import Post, Comment, User
from django.contrib.auth.forms import UserCreationForm, UserChangeForm


class PostForm(forms.ModelForm):
    class Meta():
        model = Post
        fields = ('author', 'title', 'text')

        widgets = {
            'title': forms.TextInput(attrs={'class': 'textinputclass'}),
            'text': forms.Textarea(attrs={
                'class': 'editable medium-editor-textarea postcontent '})
        }


class CommentForm(forms.ModelForm):
    class Meta():
        model = Comment
        fields = ('author', 'text')

        widgets = {
            'author': forms.TextInput(attrs={'class': 'textinputclass'}),
            'text': forms.Textarea(attrs={
                'class': 'editable medium-editor-textarea postcontent'})
        }


class CustomUserCreationForm(UserCreationForm):

    class Meta(UserCreationForm):
        model = User
        fields = ('email',)
