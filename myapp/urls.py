from django.urls import path, include
from . import views
from .views import PostListView, PostDetailView, PostCreateView, CustomLoginView
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('', views.home, name='home'),
    path('create/', views.create_post, name='create_post'),
    path('posts/', PostListView.as_view(), name='post_list'),
    path('posts/<int:pk>/', PostDetailView.as_view(), name='post_detail'),
    path('create/', PostCreateView.as_view(), name='create_post'),
    path('accounts/profile/', views.account_home, name='account_home'),
    path('accounts/', include('django.contrib.auth.urls')),
    path('accounts/logout/', auth_views.LogoutView.as_view(), name='logout'),
    path('accounts/login/', CustomLoginView.as_view(), name='login'),
]
