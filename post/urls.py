from django.conf.urls import url
from . import views

app_name = 'post'

urlpatterns = [

    url(r'^$', views.all_post, name='all_post'),
    url(r'^(?P<id>\d+)$', views.post, name='post'),

    

    url(r'^login$', views.login, name='login'),
    url(r'^signup$', views.signup, name='signup'),



    url(r'^create$', views.create_post, name='create_post'),
    url(r'^(?P<id>\d+)/edit$', views.edit_post, name='edit_post'),
]
