# review/models.py
from django.db import models
from hospital.models import Hospital
from users.models import User  # 유저 모델 import

class Review(models.Model):
    hospital = models.ForeignKey(Hospital, on_delete=models.CASCADE, related_name='reviews')  # 중요!
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    rating = models.IntegerField()
    cost_reasonable = models.BooleanField()
    teen_friendly = models.BooleanField()
    doctor_name = models.CharField(max_length=100, blank=True)  # 담당의
    diagnosis = models.CharField(max_length=100, blank=True)    # 진료질환
    is_kind = models.BooleanField(default=False)  # ✅ 친절해요 키워드
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

class ReviewLike(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    review = models.ForeignKey(Review, on_delete=models.CASCADE, related_name='likes')
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        unique_together = ('user', 'review')  # 유저 당 하나의 좋아요만 허용
