from django.http import HttpResponse, HttpRequest
from django.shortcuts import render
from dataclasses import dataclass
from blog.services import lista

# from mathematics.services import AlgebraService
from django.template.loader import render_to_string


@dataclass
class Post:
    id:int
    title:str
    content:str




def posts_list(request):
    posts = [Post(id=1, title=f'tresc posta {idx}', content=f'content posta nr {idx}') for idx in range(10)]
    return render(
        request=request,
        template_name="blog.html",
        context={'posts': posts})

def post_detail(request,id:int):
    posts = [Post(id=1, title=f'tresc posta {idx}', content=f'content posta nr {idx}') for idx in range(10)]
    return render(
        request=request,
        template_name="post.html",
        context={'post': posts[id]})