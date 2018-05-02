from django.conf.urls import url
from accounts.views import Login, Logout
from . import views

app_name = 'accounts'

urlpatterns = [
    url(r'^login/$', Login.as_view(), name='login'),
    url(r'^logout/$', Logout.as_view(), name='logout'),
    # url(r'^dashboard/$', views.dashboard, name='dashboard'),
]
