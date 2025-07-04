from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from django.http import JsonResponse
from posts.models import Post, Comment, Scrap
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
    comments = Comment.objects.filter(post=post).select_related('user').order_by('created_at') # 해당 게시글의 댓글 가져오기

    # 해당 게시글의 전체 댓글 개수 계산
    total_comment_count = comments.count()

    # 일반회원-익명/전문의회원-실명 구분
    processed_comments = []
    for comment in comments:
        comment_author_display_name = "익명"
        if comment.user.is_doctor:
            display_parts = [comment.user.username] # 전문의인 경우 실명
            if comment.user.position:
                display_parts.append(comment.user.position) # 직급 표시
            hospital_info = ""
            if comment.user.hospital:
                hospital_info = f"({comment.user.hospital})" # 소속 병원 표시
            comment_author_display_name = " ".join(display_parts)
            if hospital_info:
                comment_author_display_name += f" {hospital_info}"

        processed_comments.append({
            'comment': comment,
            'display_name': comment_author_display_name
        })

    # 사용자 나이 계산
    today = date.today()
    birth_date = post.user.date_of_birth
    age = today.year - birth_date.year - ((today.month, today.day) < (birth_date.month, birth_date.day))

    # 댓글 생성 처리 (POST 요청)
    if request.method == 'POST':
        comment_content = request.POST.get('comment_content')
        # 임시 사용자 (DB의 첫 번째 사용자)를 가져옴 ***********
        # request.user로 대체해야 함
        temp_user = User.objects.first()
        if temp_user and comment_content:
            Comment.objects.create(post=post, user=temp_user, content=comment_content)
            return redirect('posts:post_detail', post_id=post.id)

    # 스크랩 여부 확인
    is_scrapped = False
    # 임시 사용자 (DB의 첫 번째 사용자)를 가져옴 ***********
    # request.user로 대체해야 함
    temp_user = User.objects.first()
    if temp_user:
        is_scrapped = Scrap.objects.filter(user=temp_user, post=post).exists()

    context = {
        'post': post,
        'comments': processed_comments,
        'author_age': age,
        'is_scrapped': is_scrapped,
        'total_comment_count': total_comment_count,
    }
    return render(request, 'posts/post_detail.html', context)

#@login_required
def toggle_scrap(request, post_id):
    if request.method == 'POST': # POST 요청만 허용
        post = get_object_or_404(Post, pk=post_id)
        # 임시 사용자 (DB의 첫 번째 사용자)를 가져옴 ***********
        # request.user로 대체해야 함
        temp_user = User.objects.first()
        if not temp_user:
            return JsonResponse({'error': 'No user available for testing'}, status=400)
        scrap, created = Scrap.objects.get_or_create(user=temp_user, post=post)
        if not created:
            scrap.delete()
            return JsonResponse({'scrapped': False})
        else:
            return JsonResponse({'scrapped': True})
    return JsonResponse({'error': 'Invalid request method'}, status=400)

def post_search(request):
    # 검색 로직 여기에 구현
    return render(request, 'posts/post_search.html')


def my_questions(request):
    # 임시 사용자 (DB의 첫 번째 사용자)를 가져옴 ***********
    # request.user로 대체해야 함
    temp_user = User.objects.first()
    my_posts = []
    if temp_user:
        my_posts = Post.objects.filter(user=temp_user).order_by('-created_at')

    context = {
        'my_posts': my_posts
    }
    return render(request, 'posts/my_questions.html', context)