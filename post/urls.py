from django.conf.urls import url
from django.urls import path
from . import views

app_name = 'post'

urlpatterns = [

    path('', views.all_post, name='all_post'),
    path('<int:id>/', views.post, name='post'),
    path('login/', views.login_view, name='login'),
    path('signup/', views.signup, name='signup'),
    path('create/', views.create_post, name='create_post'),
    path('logout/', views.logout_view, name='logout'),
    path('<int:id>/edit/', views.edit_post, name='edit_post'),
]
