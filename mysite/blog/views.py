from django.shortcuts import render
from django.urls import path

def post_list(request): 
    return render(request, 'blog/post_list.html', {})