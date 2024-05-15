from django.urls import path
from . import views
from .views import PostListView, PostDetailView, PostCreateView
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('', views.home, name='home'),
    # path('posts/', views.post_list, name='post_list'),
    path('create/', views.create_post, name='create_post'),
    path('posts/', PostListView.as_view(), name='post_list'),
    path('posts/<int:pk>/', PostDetailView.as_view(), name='post_detail'),
    path('create/', PostCreateView.as_view(), name='create_post'),
    path('accounts/profile/', views.account_home, name='account_home'),
]
