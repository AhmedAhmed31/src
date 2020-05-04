from django.shortcuts import render, get_object_or_404, redirect
from .models import CV
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth import login,logout


def about_me(request):

    return render(request, 'CV.html')