from django.urls import path
from . import views


urlpatterns=[
    path('blog/posts/', views.posts_list, name="posts-list"),
    path('blog/posts/<int:id>', views.post_detail, name="post-details"),
]
