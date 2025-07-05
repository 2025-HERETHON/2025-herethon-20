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
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
