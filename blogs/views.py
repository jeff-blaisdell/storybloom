from django.shortcuts import render
from blogs.models import Post

def index(request):
    context = {'posts': Post.objects.all()}
    return render(request, 'blogs/index.html', context)
