from django import forms
from .models import Comment, Post


class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ('user', 'email', 'body')


class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ('title', 'content', 'category', 'seo_title', 'seo_description', 'status',)


class LoginForm(forms.Form):
    username = forms.CharField(
        widget=forms.TextInput(
            attrs={'class': 'form-control'}))
    password = forms.CharField(
        widget=forms.PasswordInput(
            attrs={'class': 'form-control'}))
