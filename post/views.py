from django.shortcuts import render, get_object_or_404, redirect
from .models import Post
from .forms import PostForm
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth import login


# Create your views here.
def all_post(request):
    all_posts = Post.objects.filter(Publish=True)
    context = {
        'all': all_posts,
    }
    return render(request, 'allpost.html', context)


def post(request, id):
    post = get_object_or_404(Post, id=id)
    context = {
        'post': post,
    }
    return render(request, 'single_post.html', context)


def signup(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('/')

    else:
        form = UserCreationForm()

    context = {
        'form': form,
    }

    return render(request, 'signup.html', context)


def login_view(request):
    if request.method == 'POST':
        form = AuthenticationForm(data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            return redirect('/')
    else:

        form = AuthenticationForm()

    context = {
        'form': form,
    }
    return render(request, 'login.html', context)


def edit_post(request, id):
    post = get_object_or_404(Post, id=id)
    if request.method == 'POST':
        form = PostForm(request.POST, request.FILES, instance=post)
        if form.is_valid():
            new_form = form.save(commit=False)
            new_form.user = request.user
            new_form.save()
            return redirect('/')

    else:
        form = PostForm(instance=post)

    context = {
        'form': form,
    }

    return render(request, 'edit.html', context)


def create_post(request):
    if request.method == 'POST':
        form = PostForm(request.POST, request.FILES)
        if form.is_valid():
            new_form = form.save(commit=False)
            new_form.user = request.user
            new_form.save()
            return redirect('/')

    else:
        form = PostForm()

    context = {
        'form': form

    }
    return render(request, 'create.html', context)


def about_me(request):
    pass
