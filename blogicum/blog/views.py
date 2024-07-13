from django.shortcuts import get_object_or_404, render

from blog.models import Category, Post

POSTS_ON_MAIN = 5


def index(request):
    post_list = Post.published.published().select_related(
        'category', 'author', 'location'
    )[:POSTS_ON_MAIN]
    context = {'post_list': post_list}
    return render(request, 'blog/index.html', context)


def post_detail(request, post_id):
    post = get_object_or_404(
        Post.published.published().select_related(
            'category',
            'author',
            'location'
        ).filter(pk=post_id)
    )
    context = {'post': post}
    return render(request, 'blog/detail.html', context)


def category_posts(request, category_slug):
    category = get_object_or_404(
        Category,
        slug=category_slug,
        is_published=True,
    )
    post_list = Post.published.published().select_related(
        'category',
        'author',
        'location'
    ).filter(category=category)
    context = {
        'category': category,
        'post_list': post_list,
    }
    return render(request, 'blog/category.html', context)
