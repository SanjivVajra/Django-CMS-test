from django import forms
from .models import Comment, Post, Category


class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ('user', 'email', 'body')


class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ('title', 'content', 'category', 'seo_title', 'seo_description', 'status',)


class CategoryForm(forms.ModelForm):
    class Meta:
        model = Category
        fields = ('name',)


class InBlogCommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ('body',)
