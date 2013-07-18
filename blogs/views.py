from django.shortcuts import render
from blogs.models import Post

def index(request):
    context = {'posts': Post.objects.all()}
    return render(request, 'blogs/index.html', context)

def get_category(request, category_id):
    context = {'post': Post.objects.get(category=category_id) }
    return render(request, 'blogs/category.html', context)

def get_post(request, category_id, post_id):
    context = {'post': Post.objects.get(id=post_id) }
    return render(request, 'blogs/post.html', context)