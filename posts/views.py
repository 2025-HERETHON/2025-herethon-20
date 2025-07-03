from django.shortcuts import render, get_object_or_404
from posts.models import Post, Category

def post_list(request, category_slug=None):
    # 모든 게시글 가져오기
    posts = Post.objects.all()
    current_category = None

    if category_slug:
        # URL에서 카테고리 슬러그를 받아 카테고리 객체 가져오기
        current_category = get_object_or_404(Category, slug=category_slug)
        posts = posts.filter(category=current_category)  # 해당 카테고리에 속하는 게시글만 필터링

    # 모든 카테고리 목록 (네비게이션 바에 표시하기 위해 필요)
    categories = Category.objects.all()

    context = {
        'posts': posts,
        'current_category': current_category,
        'categories': categories,
    }

    return render(request, 'posts/post_list.html', context)