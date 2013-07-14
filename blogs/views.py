from django.shortcuts import render
from blogs.models import Post

def index(request):
    context = {'posts': Post.objects.all()}
    return render(request, 'blogs/index.html', context)

def view_post(request, post_id):
    context = {'post': Post.objects.get(id=post_id) }
    return render(request, 'blogs/post.html', context)