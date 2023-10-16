from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='home'),
    path('blogs/', views.post_list, name='blogs'),
    path('blogs/<slug:slug>/', views.post_detail, name='blog'),
    path('like_post/<slug:slug>/', views.like_post, name='like_post'),
    path('profile/<str:username>/', views.user_profile, name='profile')
]
    