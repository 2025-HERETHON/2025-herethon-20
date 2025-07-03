from django.db import models

class User(models.Model):
    username = models.CharField(max_length=10, unique=True)
    password = models.CharField(max_length=15)
    email = models.EmailField(unique=True)
    date_of_birth = models.DateField()
    is_doctor = models.BooleanField(default=False)
    hospital = models.CharField(max_length=30, null=True, blank=True)
    position = models.CharField(max_length=30, null=True, blank=True)
    phone_number = models.CharField(max_length=20)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.username