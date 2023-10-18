from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='home'),
    path('create_post/', views.create_post, name='create_post'),
    path('blogs/', views.post_list, name='blogs'),
    path('blogs/<slug:slug>/', views.post_detail, name='blog'),
    path('blogs/modify_post/<slug:slug>/', views.modify_post, name='modify_post'),
    path('blogs/delete_post/<slug:slug>/', views.delete_post, name='delete_post'),
    path('like_post/<slug:slug>/', views.like_post, name='like_post'),
    path('profile/<str:username>/', views.user_profile, name='profile')
]
    