from django.urls import path

from .views import PostListView, create_user

urlpatterns = [
    path('', PostListView.as_view(), name='post_list'),
    path('create/', create_user)
]