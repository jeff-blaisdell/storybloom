from django.contrib import admin
from blogs.models import Post
from blogs.models import Category

admin.site.register(Post)
admin.site.register(Category)