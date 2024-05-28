from django.shortcuts import render, redirect
from .models import Post
from .forms import PostForm
from django.contrib.auth.decorators import login_required
from django.views.generic import ListView, DetailView, CreateView
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.views import LoginView


class CustomLoginView(LoginView):
    template_name = 'registration/login.html'
    authentication_form = AuthenticationForm


def home(request):
    return render(request, 'home.html')


@login_required(login_url='/accounts/login')
def account_home(request):
    return render(request, 'account_home.html', {'user': request.user})


def post_list(request):
    posts = Post.objects.all()
    return render(request, 'post_list.html', {'posts': posts})


@login_required(login_url='/accounts/login')
def create_post(request):
    if request.method == 'POST':
        form = PostForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('post_list')
    else:
        form = PostForm()
    return render(request, 'create_post.html', {'form': form})


class PostDetailView(DetailView):
    model = Post
    template_name = 'post_detail.html'


class PostListView(ListView):
    model = Post
    template_name = 'post_list.html'
    context_object_name = 'posts'


class PostCreateView(CreateView):
    model = Post
    fields = ['title', 'content', 'image', 'type']
    template_name = 'create_post.html'
    success_url = '/posts/'
