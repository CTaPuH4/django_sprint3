from django.shortcuts import get_object_or_404, render
from blog.models import Post, Category
from django.utils import timezone


def index(request):
    post_list = Post.objects.select_related(
        'category', 'author', 'location'
    ).filter(
        is_published=True,
        category__is_published=True,
        pub_date__lte=timezone.now(),
    )[0:5]
    context = {'post_list': post_list}
    return render(request, 'blog/index.html', context)


def post_detail(request, post_id):
    post = get_object_or_404(
        Post.objects.select_related(
            'category',
            'author',
            'location'
        ).filter(
            pk=post_id,
            is_published=True,
            pub_date__lte=timezone.now(),
            category__is_published=True
        )
    )
    context = {'post': post}
    return render(request, 'blog/detail.html', context)


def category_posts(request, category_slug):
    category = get_object_or_404(
        Category.objects.filter(
            slug=category_slug,
            is_published=True,
        )
    )
    post_list = Post.objects.select_related(
        'category',
        'author',
        'location'
    ).filter(
        is_published=True,
        pub_date__lte=timezone.now(),
        category__slug=category_slug,
    )

    context = {
        'category': category,
        'post_list': post_list,
    }
    return render(request, 'blog/category.html', context)
