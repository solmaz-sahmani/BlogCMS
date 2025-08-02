from django.shortcuts import render, redirect
from .forms import RegistrationForm
from django.contrib.auth import login
from django.contrib.auth.views import LoginView, LogoutView
from django.http import HttpResponse
from .forms import PostForm
from .models import Post
from django.shortcuts import get_list_or_404
from django.contrib.auth.decorators import login_required

# Create your views here.
def index(request):
    posts = Post.objects.all().order_by('-created_date')
    return render (request, 'blog/index.html', {'posts': posts})

def post_detail(request, slug):
    post = get_list_or_404(Post, slug=slug)
    return render(request, 'blog/post_detail.html', {'post': post})

def register (request):
    if request.method == 'POST':
        form = RegistrationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('index')
    else:
        form = RegistrationForm()
    return render(request, 'blog/register.html',{'form':form})

class CustomLoginView(LoginView):
    template_name = 'blog/login.html'

class CustomLogoutView(LogoutView):
    next_page = 'index'
    

@login_required
def create_post(request):
    if request.method == 'POST':
        form = PostForm(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user    
            post.save()
            return redirect('post_detail', slug=post.slug)
    else:
        form = PostForm()
    return render(request, 'blog/create_post.html', {'form': form})