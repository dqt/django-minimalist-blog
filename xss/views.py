from blog.xss.models import Blog, Category
from django.shortcuts import render_to_response, get_object_or_404


def index(request):
    return render_to_response('index.html', {
        'categories': Category.objects.all(),
        'posts': reversed(Blog.objects.all()[:5])
    })


def view_post(request, slug):
    categories = Category.objects.all()
    return render_to_response('view_post.html', {
        'categories': categories,
        'post': get_object_or_404(Blog, slug=slug)
    })


def view_category(request, slug):
    categories = Category.objects.all()
    category = get_object_or_404(Category, slug=slug)
    return render_to_response('view_category.html', {
        'categories': categories,
        'category': category,
        'posts': reversed(Blog.objects.filter(category=category)[:5])
    })
