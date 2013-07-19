from django.shortcuts import render
from blogs.models import Post, Category

def index(request):
    context = {
        'categories': Category.objects.all(),
        'posts': Post.objects.all()
    }
    return render(request, 'blogs/index.html', context)

def get_category(request, category_id):
    context = { 
        'categories': Category.objects.all(),
        'category': Category.objects.get(id=category_id),
        'posts': Post.objects.filter(category=category_id) 
    }
    return render(request, 'blogs/category.html', context)

def get_post(request, category_id, post_id):
    context = {
        'categories': Category.objects.all(),
        'post': Post.objects.get(id=post_id) 
    }
    return render(request, 'blogs/post.html', context)