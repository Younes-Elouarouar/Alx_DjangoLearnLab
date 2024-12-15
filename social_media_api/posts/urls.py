from django.urls import path
from . import views

urlpatterns = [
    path('', views.PostListView.as_view(), name='post_list'),
    path('like/<int:pk>/', views.like_post, name='like_post'),
    path('unlike/<int:pk>/', views.unlike_post, name='unlike_post'),
    path('feed/', views.user_feed, name='user_feed'),
]
