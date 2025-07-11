from django.db import models
from django.contrib.auth.models import AbstractUser

from hospital.models import Hospital

class User(AbstractUser):
    USERNAME_FIELD = 'username'
    REQUIRED_FIELDS = ['date_of_birth', 'phone_number']
    date_of_birth = models.DateField()
    is_doctor = models.BooleanField(default=False)
    hospital = models.ForeignKey(Hospital, on_delete=models.SET_NULL, null=True, blank=True)
    position = models.CharField(max_length=30, null=True, blank=True)
    phone_number = models.CharField(max_length=20)

    def __str__(self):
        return self.username

    class Meta:
        verbose_name = 'User'
        verbose_name_plural = 'Users'