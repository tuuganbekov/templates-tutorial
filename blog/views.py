from django.shortcuts import render
from django.views.generic import ListView

from .models import Post, Category


def main_page(request):
    post_list = [
        {'title': 'Post 1', 'body': 'Post 1 body'},
        {'title': 'Post 2', 'body': 'Post 2 body'},
        {'title': 'Post 3', 'body': 'Post 3 body'},
        {'title': 'Post 4', 'body': 'Post 4 body'},
    ]
    return render(request, 'blog/blog_list.html', {'posts': post_list})


def phones_list(request):
    phones = [
        {"name": "Iphone 15 pro", "price": 1000},
        {"name": "Samsung A55", "price": 500},
        {"name": "Xiaomi", "price": 650},
        {"name": "Sony", "price": 350},
    ]
    return render(request, 'blog/phone_list.html', {"phones": phones})


class PostListView(ListView):
    model = Post
    context_object_name = 'posts'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['categories'] = Category.objects.all()
        return context