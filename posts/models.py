from django.db import models
from users.models import User

CATEGORY_CHOICES = [
    ('기타', '기타'),
    ('성적자기결정권', '성적자기결정권'),
    ('여성질환', '여성질환'),
    ('피임/임신', '피임/임신'),
    ('생리', '생리'),
]

class Post(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    category = models.CharField(max_length=100, choices=CATEGORY_CHOICES)
    title = models.CharField(max_length=100)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title

class Scrap(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='scraps')
    post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name='scrapped_by')
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        unique_together = ('user', 'post')

class Comment(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    is_deleted = models.BooleanField(default=False)

    def __str__(self):
        return f'Comment by {self.user} on {self.post}'

class Notification(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='notifications', help_text="알림을 받을 사용자")
    post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name='notifications', help_text="답변이 달린 게시글")
    message = models.CharField(max_length=255)
    comment_content = models.TextField(blank=True, null=True, help_text="달린 답변 내용")
    created_at = models.DateTimeField(auto_now_add=True)
    is_read = models.BooleanField(default=False)
    notification_type = models.CharField(max_length=50, blank=True, null=True)

    class Meta:
        ordering = ['-created_at']  # 최신 알림이 먼저 보이도록

    def __str__(self):
        return f'{self.user.username} - {self.message} (읽음: {self.is_read})'