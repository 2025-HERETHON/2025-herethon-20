from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from posts.models import Scrap, Comment
from users.models import User

#@login_required
def my_scrap_post(request):
    # 임시 사용자 (DB의 첫 번째 사용자)를 가져옴 ***********
    # request.user로 대체해야 함
    temp_user = User.objects.first()
    scraps_with_details = []  # 스크랩된 게시글과 추가 정보를 담을 리스트
    if temp_user:
        scraps = Scrap.objects.filter(user=temp_user).select_related('post').order_by('-created_at')
        for scrap in scraps:
            post = scrap.post
            comment_count = Comment.objects.filter(post=post).count()
            scraps_with_details.append({
                'scrap': scrap,
                'post': post,
                'comment_count': comment_count,
            })
    return render(request, 'users/my_scrap_post.html', {'scraps_with_details': scraps_with_details})
