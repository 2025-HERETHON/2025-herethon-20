from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from django.http import JsonResponse, HttpResponse
from posts.models import Post, Comment, Scrap, Notification
from datetime import date, timedelta
from django.db.models import Q, Count, Sum
from django.utils import timezone
from users.models import User

CATEGORIES = [
    {'name': '생리', 'slug': 'saengri'},
    {'name': '피임/임신', 'slug': 'piim'},
    {'name': '여성질환', 'slug': 'yeoseongjilhwan'},
    {'name': '성적자기결정권', 'slug': 'seongjeogjagi'},
    {'name': '기타', 'slug': 'gita'},
]

def post_list(request, category_slug=None):
    # 모든 게시글 가져오기
    posts = Post.objects.annotate(
        comment_count=Count('comment', filter=Q(comment__is_deleted=False, comment__parent_comment__isnull=True))
    ).order_by('-created_at')
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

def doctor_post_list(request, category_slug=None):
    # 모든 게시글 가져오기
    posts = Post.objects.annotate(
        comment_count=Count('comment', filter=Q(comment__is_deleted=False, comment__parent_comment__isnull=True))
    ).order_by('-created_at')
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
    return render(request, 'posts/post_list_doctor.html', context)

def post_detail(request, post_id):
    post = get_object_or_404(Post, pk=post_id) # 해당 ID의 게시글 가져오기

    # 해당 게시글의 답변 수 계산 (답댓글 제외)
    comments_queryset = Comment.objects.filter(
        post=post, parent_comment__isnull=True, is_deleted=False
    ).select_related('user').order_by('created_at')
    total_comment_count = comments_queryset.count()

    # 일반회원-익명/전문의회원-실명 구분
    processed_comments = []
    for comment in comments_queryset:
        replies = comment.replies.all().select_related('user').order_by('created_at')

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

        is_comment_author = (request.user.is_authenticated and request.user == comment.user and not comment.is_deleted)

        processed_reply_comments = [] # 답댓글
        replies_queryset = comment.replies.filter(is_deleted=False).select_related('user').order_by('created_at')
        for reply in replies_queryset:
            reply_author_display_name = "익명"
            if reply.user.is_doctor:
                display_parts_reply = [reply.user.username]
                if reply.user.position:
                    display_parts_reply.append(reply.user.position)
                hospital_info_reply = ""
                if reply.user.hospital:
                    hospital_info_reply = f"({reply.user.hospital})"
                reply_author_display_name = " ".join(display_parts_reply)
                if hospital_info_reply:
                    reply_author_display_name += f" {hospital_info_reply}"

            is_reply_author = (request.user.is_authenticated and request.user == reply.user and not reply.is_deleted)

            processed_reply_comments.append({
                'comment': reply,
                'display_name': reply_author_display_name,
                'is_author': is_reply_author,
                'author_username': reply.user.username if reply.user.is_doctor else "익명",
                'author_position': reply.user.position if reply.user.is_doctor else "",
                'author_hospital': str(reply.user.hospital) if reply.user.is_doctor and reply.user.hospital else "",
            })

        processed_comments.append({
            'comment': comment,
            'display_name': comment_author_display_name,
            'replies': processed_reply_comments,
            'is_author': is_comment_author,
            'is_doctor': comment.user.is_doctor,
            'author_username': comment.user.username if comment.user.is_doctor else "익명",
            'author_position': comment.user.position if comment.user.is_doctor else "",
            'author_hospital': comment.user.hospital if comment.user.is_doctor else "",
        })

    # 사용자 나이 계산
    author_age = None
    if post.user and hasattr(post.user, 'date_of_birth') and post.user.date_of_birth:
        today = date.today()
        birth_date = post.user.date_of_birth
        author_age = today.year - birth_date.year - ((today.month, today.day) < (birth_date.month, birth_date.day))

    # 댓글 생성 처리 (POST 요청)
    if request.method == 'POST':
        comment_content = request.POST.get('comment_content')
        parent_comment_id = request.POST.get('parent_comment_id')

        if request.user.is_authenticated:
            if comment_content:
                parent_comment = None
                if parent_comment_id:
                    parent_comment = get_object_or_404(Comment, pk=parent_comment_id, is_deleted=False)

                new_comment = Comment.objects.create(
                    post=post,
                    user=request.user,
                    content=comment_content,
                    parent_comment=parent_comment
                )

                #  답변 알림 생성
                if request.user != post.user:
                    Notification.objects.create(
                        user=post.user,  # 알림을 받을 사람: 게시글 작성자
                        post=post,  # 알림의 대상 게시글
                        message='에 새로운 답변',
                        comment_content=comment_content,
                        notification_type='comment_on_my_post'  # 알림 유형
                    )

                # 답댓글 알림 생성
                if parent_comment and request.user != parent_comment.user:
                    Notification.objects.create(
                        user=parent_comment.user,  # 알림을 받을 사람: 부모 댓글 작성자
                        post=post,
                        message='내 답변에 새로운 답댓글',
                        comment_content=comment_content,
                        notification_type='reply_on_my_comment'
                    )
                return redirect('posts:post_detail', post_id=post.id)
        else:
            return redirect('users:user_selection')

    # 스크랩 여부 확인
    is_scrapped = False
    if request.user.is_authenticated:
        is_scrapped = Scrap.objects.filter(user=request.user, post=post).exists()

    # 현재 로그인된 사용자가 게시글 작성자인지 확인
    is_author = False
    if request.user.is_authenticated:
        is_author = (request.user == post.user)

    context = {
        'post': post,
        'comments': processed_comments,
        'author_age': author_age,
        'is_scrapped': is_scrapped,
        'total_comment_count': total_comment_count,
        'is_author': is_author,
    }
    return render(request, 'posts/post_detail.html', context)

@login_required
def toggle_scrap(request, post_id):
    if request.method == 'POST': # POST 요청만 허용
        post = get_object_or_404(Post, pk=post_id)
        scrap, created = Scrap.objects.get_or_create(user=request.user, post=post)
        if not created:
            scrap.delete()
            return JsonResponse({'scrapped': False})
        else:
            return JsonResponse({'scrapped': True})
    return JsonResponse({'error': 'Invalid request method'}, status=400)

def post_search(request):
    query = request.GET.get('query')
    posts = Post.objects.all()
    if query:
        posts = posts.filter(
            Q(title__icontains=query) | Q(content__icontains=query)
        ).distinct()
    context = {
        'query': query,
        'posts': posts,
        'categories': CATEGORIES,
    }
    return render(request, 'posts/post_search.html', context)

@login_required
def my_questions(request):
    my_posts = Post.objects.filter(user=request.user).order_by('-created_at')
    my_posts_count = my_posts.count()

    context = {
        'my_posts': my_posts,
        'my_posts_count': my_posts_count,
        'active_tab': 'questions',
    }
    return render(request, 'posts/my_questions.html', context)

@login_required
def my_answers(request):
    posts_with_my_comments = Post.objects.filter(
        Q(comment__user=request.user, comment__is_deleted=False) |
        Q(comment__replies__user=request.user, comment__replies__is_deleted=False)
    ).distinct()
    posts_with_my_comments = posts_with_my_comments.order_by('-created_at')

    my_comments_count = Comment.objects.filter(user=request.user, is_deleted=False).count()

    context = {
        'posts_with_my_comments': posts_with_my_comments,
        'my_comments_count': my_comments_count,
        'active_tab': 'answers', # 현재 활성화된 탭
    }
    return render(request, 'posts/my_answers.html', context)

@login_required
def create_post(request):
    initial_category_name = '생리'
    from_category_slug = request.GET.get('from_category_slug')

    if from_category_slug:
        for cat in CATEGORIES:
            if cat['slug'] == from_category_slug:
                initial_category_name = cat['name']
                break

    if request.method == 'POST':
        category = request.POST.get('category')
        title = request.POST.get('title')
        content = request.POST.get('content')

        if not all([title, content]):
            context = {
                'error_message': '제목과 내용을 모두 입력해주세요.',
                'categories': CATEGORIES,
                'selected_category': category,
                'title': title,
                'content': content,
            }
            return render(request, 'posts/create_post.html', context)

        # Post 객체 생성 및 저장
        Post.objects.create(
            user=request.user, # 현재 로그인된 사용자
            category=category,
            title=title,
            content=content,
        )
        return redirect('posts:post_list') # 게시글 목록으로 리디렉션

    else: # GET 요청일 경우 (폼 보여주기)
        context = {
            'categories': CATEGORIES,
            'selected_category': initial_category_name, # 초기 선택 카테고리 설정
        }
        return render(request, 'posts/create_post.html', context)

@login_required
def edit_post(request, post_id):
    post = get_object_or_404(Post, pk=post_id)

    # 게시글 작성자만 수정 가능하도록 권한 확인
    if request.user != post.user:
        return HttpResponse("이 게시글을 수정할 권한이 없습니다.", status=403) # 403 Forbidden 에러

    if request.method == 'POST':
        category = request.POST.get('category')
        title = request.POST.get('title')
        content = request.POST.get('content')

        if not all([title, content]):
            context = {
                'error_message': '제목과 내용을 모두 입력해주세요.',
                'categories': CATEGORIES,
                'selected_category': category, # 현재 선택된 카테고리
                'title': title,
                'content': content,
                'post_id': post_id, # 수정 모드임을 템플릿에 알림
                'is_edit_mode': True, # 수정 모드임을 템플릿에 알림
            }
            return render(request, 'posts/create_post.html', context)

        # 게시글 업데이트
        post.category = category
        post.title = title
        post.content = content
        post.save() # 변경사항 저장

        return redirect('posts:post_detail', post_id=post.id) # 수정된 게시글 상세 페이지로 리디렉션

    else: # GET 요청 (수정 폼 불러오기)
        context = {
            'categories': CATEGORIES,
            'selected_category': post.category, # 기존 게시글의 카테고리
            'title': post.title, # 기존 게시글의 제목
            'content': post.content, # 기존 게시글의 내용
            'post_id': post_id, # 수정 모드임을 템플릿에 알림 (폼 액션 URL에 사용)
            'is_edit_mode': True, # 수정 모드임을 템플릿에 알림
        }
        return render(request, 'posts/create_post.html', context)

@login_required
def delete_post(request, post_id):
    post = get_object_or_404(Post, pk=post_id)

    if request.user != post.user:
        return HttpResponse("이 게시글을 삭제할 권한이 없습니다.", status=403)  # 403 Forbidden 에러

    if request.method == 'POST':
        post.delete()  # 게시글 삭제
        return redirect('posts:post_list')  # 게시글 목록으로 리디렉션

    return HttpResponse("잘못된 접근입니다.", status=400)


@login_required
def delete_comment(request, post_id, comment_id):
    comment = get_object_or_404(Comment, pk=comment_id, post_id=post_id) # 해당 게시글의 댓글인지 확인

    # 댓글 작성자만 삭제할 수 있도록 권한 확인
    if request.user != comment.user:
        return HttpResponse("권한이 없습니다.", status=403) # 403 Forbidden 에러 반환

    # 소프트 삭제 처리
    comment.is_deleted = True
    comment.content = "삭제된 댓글입니다." # 내용도 변경하여 시각적으로 삭제됨을 표시
    comment.save()

    return redirect('posts:post_detail', post_id=post_id)