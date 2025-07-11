from django.urls import path

from .views import PostListView, create_post

urlpatterns = [
    path('', PostListView.as_view(), name='post_list'),
    path('create/', create_post)
]