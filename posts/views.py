from django.shortcuts import render, get_object_or_404, redirect
from posts.models import Post, Comment
from users.models import User
from datetime import date

CATEGORIES = [
    {'name': '생리', 'slug': 'saengri'},
    {'name': '피임/임신', 'slug': 'piim'},
    {'name': '여성질환', 'slug': 'yeoseongjilhwan'},
    {'name': '성적자기결정권', 'slug': 'seongjeogjagi'},
    {'name': '기타', 'slug': 'gita'},
]

def post_list(request, category_slug=None):
    # 모든 게시글 가져오기
    posts = Post.objects.all()
    current_category = None

    if category_slug:
        matched = next((c for c in CATEGORIES if c['slug'] == category_slug), None)
        if matched:
            current_category = matched
            posts = posts.filter(category=matched['name'])

    context = {
        'posts': posts,
        'categories': CATEGORIES,
        'current_category': current_category,
    }
    return render(request, 'posts/post_list.html', context)

def post_detail(request, post_id):
    post = get_object_or_404(Post, pk=post_id) # 해당 ID의 게시글 가져오기
    comments = Comment.objects.filter(post=post).order_by('created_at') # 해당 게시글의 댓글 가져오기

    # 사용자 나이 계산
    today = date.today()
    birth_date = post.user.date_of_birth
    age = today.year - birth_date.year - ((today.month, today.day) < (birth_date.month, birth_date.day))

    # 댓글 생성 처리 (POST 요청)
    if request.method == 'POST':
        comment_content = request.POST.get('comment_content')
        try:
            comment_user = User.objects.first() # ******** DB에 있는 첫 번째 사용자를 댓글 작성자로 지정, 추후 request.user 사용해야 함
            if comment_user and comment_content:
                Comment.objects.create(post=post, user=comment_user, content=comment_content)
                return redirect('posts:post_detail', post_id=post.id) # 댓글 작성 후 새로고침
        except User.DoesNotExist:
            # 사용자 없음 오류 처리 (디버깅용)
            pass

    context = {
        'post': post,
        'comments': comments,
        'author_age': age,
    }
    return render(request, 'posts/post_detail.html', context)