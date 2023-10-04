from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='home'),
    path('blogs/', views.post_list, name='blogs'),
    path('blogs/<slug:slug>/', views.post_detail, name='blog'),
]