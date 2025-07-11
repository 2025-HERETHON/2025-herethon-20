from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth import login as auth_login, logout as auth_logout
from django.contrib.auth.decorators import login_required
from posts.models import Scrap, Comment, Post, Notification
from users.models import User
from datetime import timedelta
from django.utils import timezone
from django.db.models import Count, Max, Exists, OuterRef, Sum, Q
from hospital.models import Hospital
from review.models import Review


# 마이페이지
@login_required
def my_page(request):
    if request.user.is_doctor:
        return render(request, 'users/mypage_doctor.html')
    else:
        return render(request, 'users/mypage.html')

@login_required
def my_scrap_post(request):
    current_user = request.user
    scraps_with_details = []
    scraps = Scrap.objects.filter(user=current_user).select_related('post').order_by('-created_at')
    for scrap in scraps:
        post = scrap.post
        comment_count = Comment.objects.filter(post=post).count()
        scraps_with_details.append({
            'scrap': scrap,
            'post': post,
            'comment_count': comment_count,
        })
    return render(request, 'users/my_scrap_post.html', {'scraps_with_details': scraps_with_details})

@login_required
def notification_settings(request):
    return render(request, 'users/notification_settings.html')

@login_required
def customer_service(request):
    return render(request, 'users/customer_service.html')

@login_required
def user_guide(request):
    return render(request, 'users/user_guide.html')

def user_selection(request):
    if request.user.is_authenticated:
        return redirect('users:user_home')
    return render(request, 'users/user_selection.html')

def login_as_user(request, user_type):
    user = None

    if user_type == 'general':
        user, created = User.objects.get_or_create(
            username='이멋사',
            defaults={
                'password': '1234',
                'email': 'likelion13@naver.com',
                'date_of_birth': '2000-01-01',
                'is_doctor': False,
                'phone_number': '01011112222'
            }
        )

    elif user_type == 'doctor':
        hospital = Hospital.objects.filter(name__icontains='여기톤병원').first()  # ✅ 병원 객체로 가져오기

        if not hospital:
            # 병원 객체 없으면 새로 생성
            hospital = Hospital.objects.create(
                name='여기톤병원',
                address='서울특별시 강남구',
                sidoCd='110000',
                sgguCd='110001',
                tel='02-0000-0000',
                is_female_doctor=True
            )

        user, created = User.objects.get_or_create(
            username='박의사',
            defaults={
                'password': '1234',
                'email': 'doctor@naver.com',
                'date_of_birth': '1985-05-10',
                'is_doctor': True,
                'hospital': hospital,  # ✅ Hospital 객체 할당
                'position': '전문의',
                'phone_number': '01033334444'
            }
        )


    if user:
        auth_login(request, user)
        print(f"로그인 성공: {user.username} (전문의: {user.is_doctor})")
        # 로그인 후 홈으로 리디렉션
        return redirect('users:user_home')

    else:
        return render(request, 'users/user_selection.html', {'error_message': '사용자를 찾거나 생성할 수 없습니다.'})

def user_logout(request):
    auth_logout(request)
    return redirect('users:user_selection')

def user_home(request):
    # 일반 홈 - 이번 주 핫 질문: 3일 이내에 작성된 글 중에서 댓글이 가장 많은 4개 게시글 가져오기
    three_days_ago = timezone.now() - timedelta(days=3)
    hot_questions = Post.objects.filter(
        created_at__gte=three_days_ago  # 3일 이내에 작성된 글 필터링
    ).annotate(
        comment_count=Count('comment', filter=Q(comment__is_deleted=False, comment__parent_comment__isnull=True))  # 각 게시글의 댓글 수 계산
    ).order_by(
        '-comment_count', '-created_at'  # 댓글 수 내림차순, 그 다음 최신순으로 정렬
    )[:4]  # 상위 4개만 가져오기

    # 일반 홈 - 방금 답변된 질문: 가장 최근에 댓글이 달린 질문 4개
    recently_commented_questions = Post.objects.annotate(
        latest_comment_time=Max('comment__created_at'),  # 각 포스트의 가장 최근 댓글 시간
        comment_count = Count('comment', filter=Q(comment__is_deleted=False, comment__parent_comment__isnull=True))
    ).filter(
        latest_comment_time__isnull=False  # 댓글이 없는 게시글 제외
    ).order_by(
        '-latest_comment_time'  # 가장 최근 댓글 시간 기준으로 내림차순 정렬
    )[:4]  # 상위 4개만 가져오기

    # 전문의 홈 - 방금 등록된 질문: 가장 최근에 작성된 질문 4개
    recently_registered_questions = Post.objects.annotate(
        comment_count=Count('comment', filter=Q(comment__is_deleted=False, comment__parent_comment__isnull=True))
    ).order_by(
        '-created_at'  # 생성 시간 기준으로 내림차순 정렬
    )[:4]  # 상위 4개만 가져오기

    # 전문의 홈 - 전문의 답변을 기다리고 있는 질문: 전문의 답변이 하나도 없는 질문 중에 가장 최근 작성 4개
    doctor_comments_exist = Comment.objects.filter(
        post=OuterRef('pk'),
        user__is_doctor=True
    )
    unanswered_doctor_questions = Post.objects.annotate(
        has_doctor_comment=Exists(doctor_comments_exist)
    ).filter(
        has_doctor_comment=False  # 전문의 댓글이 없는 게시글만 필터링
    ).annotate(
        comment_count=Count('comment', filter=Q(comment__is_deleted=False, comment__parent_comment__isnull=True))
    ).order_by(
        '-created_at'  # 최신순으로 정렬
    )[:4]  # 상위 4개만 가져오기
    latest_reviews = Review.objects.select_related('hospital', 'user').order_by('-created_at')[:4]  # ✅ 최근 리뷰 4개 가져오기
    context = {
        'hot_questions': hot_questions,  # 템플릿으로 전달할 데이터
        'recently_commented_questions': recently_commented_questions,
        'recently_registered_questions': recently_registered_questions,
        'unanswered_doctor_questions': unanswered_doctor_questions,
        'latest_reviews': latest_reviews
        ,'star_range': range(1, 6), 
    }

    if request.user.is_authenticated and request.user.is_doctor:
        # 전문의 회원
        return render(request, 'home_doctor.html', context)
    else:
        # 일반 회원
        return render(request, 'home.html', context)

@login_required
def my_notifications(request):
    notifications = Notification.objects.filter(user=request.user).order_by('is_read', '-created_at')

    context = {
        'notifications': notifications,
    }
    return render(request, 'my_notification.html', context)