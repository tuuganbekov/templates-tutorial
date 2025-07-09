from django.shortcuts import render, redirect
from django.views.generic import ListView

from .forms import TestForm, PostForm
from .models import Post, Category


def main_page(request):
    post_list = [
        {'title': 'Post 1', 'body': 'Post 1 body'},
        {'title': 'Post 2', 'body': 'Post 2 body'},
        {'title': 'Post 3', 'body': 'Post 3 body'},
        {'title': 'Post 4', 'body': 'Post 4 body'},
    ]
    user_list = []
    return render(
        request, 'blog/blog_list.html', 
        {
            'posts': post_list,
            'users': user_list
        }
        )


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
        # print(f"CONTEXT: {context}")
        return context
    

def create_user(request):
    if request.method == "POST":
        form = TestForm(request.POST)
        if form.is_valid():
            print(f"valid data: {form.cleaned_data}")
            # work with data
            return redirect('post_list')
    else:
        form = TestForm()
    return render(request, 'blog/bio.html', {'form': form})