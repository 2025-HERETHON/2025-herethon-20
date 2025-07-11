# reserve/views.py

from django.shortcuts import render
from users.models import User
from posts.models import Comment
from django.utils import timezone
from datetime import timedelta
from django.db.models import Count, Q

def recommended_doctors(request):
    one_week_ago = timezone.now() - timedelta(days=7)

    # 의사 중 최근 일주일 간 댓글 수 집계 + 내림차순 정렬
    doctors = (
        User.objects
        .filter(is_doctor=True)
        .annotate(
            recent_comment_count=Count(
                'comment',
                filter=Q(comment__created_at__gte=one_week_ago)
            )
        )
        .order_by('-recent_comment_count')  # 댓글 많은 순
    )

    return render(request, 'reserve/recommended_doctors.html', {
        'doctors': doctors,
    })
