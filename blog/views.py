from django.http import HttpResponse, HttpRequest
from django.shortcuts import render


from .services import FakePostService

posts = FakePostService.list()

def posts_list(request, posts=posts):
    # posts = [Post(id=idx, title=f'tresc posta {idx}', content=f'content posta nr {idx}') for idx in range(10)]
    return render(
        request=request,
        template_name="blog.html",
        context={'posts': posts})


def post_detail(request, id: int, posts=posts, ):
    # posts = [Post(id=idx, title=f'tresc posta {idx}', content=f'content posta nr {idx}') for idx in range(10)]
    return render(
        request=request,
        template_name="post.html",
        context={'post': posts[id]})
