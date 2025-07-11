# hospital/models.py
from django.db import models
from django.conf import settings
#from .models import Review

class Hospital(models.Model):
    yadmCd = models.CharField(max_length=20, unique=True)
    name = models.CharField(max_length=100)
    address = models.CharField(max_length=255)
    sidoCd = models.CharField(max_length=10)
    sgguCd = models.CharField(max_length=10)
    tel = models.CharField(max_length=20, blank=True, null=True)
    is_female_doctor = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"[{self.sidoCd}] {self.name}"
    

