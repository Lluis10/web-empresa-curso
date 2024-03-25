from django.shortcuts import render, get_object_or_404
from .models import Post, Category
# Create your views here.


def blog(request):

    posts = Post.objects.all()
    html_resposnse = render(request, "blog/blog.html", {"posts": posts})

    return html_resposnse


def category(request, category_id):
    category = get_object_or_404(Category, id=category_id)
    posts = category.get_posts.all
    html_resposnse = render(request, "blog/blog.html",
                            {"posts": posts})

    return html_resposnse
