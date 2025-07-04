from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth import login as auth_login, logout as auth_logout
from django.contrib.auth.decorators import login_required
from posts.models import Scrap, Comment, Post
from users.models import User
from datetime import date

# 마이페이지
@login_required
def my_page(request):
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
        return redirect('posts:post_list')
    return render(request, 'users/user_selection.html')

def login_as_user(request, user_type):
    user = None
    if user_type == 'general':
        user, created = User.objects.get_or_create(
            username='이멋사',
            password='1234',
            email='likelion13@naver.com',
            date_of_birth='2000-01-01',
            is_doctor=False,
            phone_number='01011112222'
        )
    elif user_type == 'doctor':
        user, created = User.objects.get_or_create(
            username='박의사',
            password='1234',
            email='doctor@naver.com',
            date_of_birth='1985-05-10',
            is_doctor=True,
            hospital='여기톤병원',
            position='전문의',
            phone_number='01033334444'
        )

    if user:
        auth_login(request, user)
        print(f"로그인 성공: {user.username} (전문의: {user.is_doctor})")
        # 로그인 후 게시글 목록 페이지로 리디렉션
        return redirect('posts:post_list')
    else:
        return render(request, 'users/user_selection.html', {'error_message': '사용자를 찾거나 생성할 수 없습니다.'})

def user_logout(request):
    auth_logout(request)
    return redirect('users:user_selection')