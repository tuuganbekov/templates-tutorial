from django.urls import path

from .views import PostListView, create_user

urlpatterns = [
    path('list/', PostListView.as_view(), name='post_list'),
    path('create/', create_user)
]