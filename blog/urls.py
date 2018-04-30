from django.conf.urls import url
from . import views

app_name = 'blog'

urlpatterns = [
    url(r'^$', views.list_of_post, name='list_of_post'),
    url(r'^draft/$', views.draft_list_of_post, name='draft_list_of_post'),
    url(r'^(?P<slug>[-\w\s]+)/$', views.post_detail, name='post_detail'),
    url(r'^(?P<slug>[-\w\s]+)/comment/$', views.add_comment, name='add_comment'),
    url(r'^category/(?P<category_slug>[-\w\s]+)/$', views.list_of_post_by_category, name='list_of_post_by_category'),
    url(r'^backend/post/new/$', views.new_post, name='new_post'),
    url(r'^backend/post/$', views.list_of_post_backend, name='list_of_post_backend'),
    # url(r'^backend/post/(?P<slug>[-\w\s]+)$', views.list_of_post_backend, name='list_of_post_backend'),
    url(r'^backend/(?P<slug>[-\w\s]+)/edit$', views.edit_post, name='edit_post'),
    url(r'^backend/(?P<slug>[-\w\s]+)/delete$', views.delete_post, name='delete_post'),
    url(r'^backend/category/new/$', views.new_category, name='new_category'),
]
