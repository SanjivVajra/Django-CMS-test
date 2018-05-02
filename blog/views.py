from django.shortcuts import render, get_object_or_404, redirect
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.http import Http404
from django.contrib import messages
from .models import Post, Category
from .forms import CommentForm, PostForm, CategoryForm, InBlogCommentForm


# Create your views here.
def list_of_post(request):
    post = Post.objects.filter(status='published')
    paginator = Paginator(post, 3)
    page = request.GET.get('page')
    try:
        posts = paginator.page(page)
    except PageNotAnInteger:
        posts = paginator.page(1)
    except EmptyPage:
        posts = paginator.page(paginator.num_pages)
    template = 'blog/post/list_of_post.html'
    context = {'posts': posts, 'page': page}
    return render(request, template, context)


def list_of_post_by_category(request, category_slug):
    categories = Category.objects.all()
    post = Post.objects.filter(status='published')
    if category_slug:
        category = get_object_or_404(Category, slug=category_slug)
        post = post.filter(category=category)
    template = 'blog/category/list_of_post_by_category.html'
    context = {'categories': categories, 'post': post, 'category': category}
    return render(request, template, context)


def draft_list_of_post(request):
    post = Post.objects.filter(status='draft')
    template = 'blog/post/draft_list_of_post.html'
    context = {'post': post}
    return render(request, template, context)


def post_detail(request, slug):
    post = get_object_or_404(Post, slug=slug)
    form = InBlogCommentForm(request.POST)
    user = request.user
    if request.method == 'POST':
        if form.is_valid():
            comment = form.save(commit=False)
            comment.post = post
            user.save()
            comment.save()
            return redirect('blog:post_detail', slug=post.slug)
        else:
            form = CommentForm()
    if post.status == 'published':
        template = 'blog/post/post_detail.html'
    else:
        template = 'blog/post/post_preview.html'
    context = {'post': post}
    return render(request, template, context)


def add_comment(request, slug):
    post = get_object_or_404(Post, slug=slug)
    form = CommentForm(request.POST)
    if request.method == 'POST':
        if form.is_valid():
            comment = form.save(commit=False)
            comment.post = post
            comment.save()
            return redirect('blog:post_detail', slug=post.slug)
        else:
            form = CommentForm()
    template = 'blog/post/add_comment.html'
    context = {'form': form}
    return render(request, template, context)


# def add_in_blog_comment(request, slug):
#     post = get_object_or_404(Post, slug=slug)
#     form = InBlogCommentForm(request.POST)
#     user = request.user
#     if request.method == 'POST':
#         if form.is_valid():
#             comment = form.save(commit=False)
#             comment.post = post
#             user.save()
#             comment.save()
#             return redirect('blog:post_detail', slug=post.slug)
#         else:
#             form = CommentForm()
#     template = 'blog/post/post_detail.html'
#     context = {'form': form}
#     return render(request, template, context)


########
# BACKEND
########
def new_post(request):
    if request.user.is_authenticated():
        if request.method == "POST":
            form = PostForm(request.POST)
            if form.is_valid():
                post = form.save(commit=False)
                post.author = request.user
                post.save()
                return redirect('blog:post_detail', slug=post.slug)
        else:
            form = PostForm()
        template = 'blog/backend/new_post.html'
        context = {'form': form}
        return render(request, template, context)
    else:
        return redirect('blog:list_of_post')


def list_of_post_backend(request):
    if request.user.is_authenticated():
        post = Post.objects.all()
        paginator = Paginator(post, 5)
        page = request.GET.get('page')
        try:
            posts = paginator.page(page)
        except PageNotAnInteger:
            posts = paginator.page(1)
        except EmptyPage:
            posts = paginator.page(paginator.num_pages)
        template = 'blog/backend/list_of_post_backend.html'
        context = {'posts': posts, 'page': page}
        return render(request, template, context)
    else:
        return redirect('blog:list_of_post')


def edit_post(request, slug):
    if request.user.is_authenticated():
        post = get_object_or_404(Post, slug=slug)
        if request.method == 'POST':
            form = PostForm(request.POST, instance=post)
            if form.is_valid():
                post = form.save(commit=False)
                post.author = request.user
                post.save()
                return redirect('blog:list_of_post_backend')
        else:
            form = PostForm(instance=post)
        template = 'blog/backend/new_post.html'
        context = {'form': form}
        return render(request, template, context)
    else:
        return redirect('blog:list_of_post')


def delete_post(request, slug):
    if request.user.is_authenticated():
        if not request.user.is_staff or not request.user.is_superuser:
            raise Http404
        post = get_object_or_404(Post, slug=slug)
        post.delete()
        messages.success(request, "Successfully Deleted")
        return redirect('blog:list_of_post_backend')
    else:
        return redirect('blog:list_of_post')


def new_category(request):
    if request.user.is_authenticated():
        if request.method == "POST":
            form = CategoryForm(request.POST)
            if form.is_valid():
                category = form.save(commit=False)
                category.save()
                # print(category.save())
                return redirect('blog:new_post')
        else:
            form = CategoryForm()
        template = 'blog/backend/new_category.html'
        context = {'form': form}
        return render(request, template, context)
    else:
        return redirect('blog:list_of_post')
