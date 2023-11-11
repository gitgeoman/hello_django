from django.urls import path
from . import views

app_name='post'
urlpatterns=[
    path('blog/posts/', views.posts_list, name="list"),
    path('blog/posts/<int:id>', views.post_detail, name="details"),
]
