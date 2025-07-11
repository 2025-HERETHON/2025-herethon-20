# reserve/views.py

from django.shortcuts import render
from users.models import User
from posts.models import Comment
from django.utils import timezone
from datetime import timedelta
from django.db.models import Count, Q

def recommended_doctors(request):
    one_week_ago = timezone.now() - timedelta(days=7)

    doctors = User.objects.filter(is_doctor=True)
    doctor_list = []

    for doctor in doctors:
        recent_comment_count = Comment.objects.filter(
            user=doctor,
            created_at__gte=one_week_ago
        ).count()

        doctor_list.append({
            'username': doctor.username,
            'hospital': {
                'name': doctor.hospital.name if doctor.hospital else '미지정',
                'tel': doctor.hospital.tel if doctor.hospital else 'N/A'
            },
            'profile_image': {
                'url': doctor.profile_image.url if doctor.profile_image else '/static/hospital/images/default_doctor.png'
            },
            'recent_comment_count': recent_comment_count,
        })

    return render(request, 'reserve/recommended_doctors.html', {'doctors': doctor_list})
