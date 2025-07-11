from django import forms
from .models import Review

class ReviewForm(forms.ModelForm):
    class Meta:
        model = Review
        fields = ['rating',
            'cost_reasonable',
            'teen_friendly',
            'is_kind',
            'doctor_name',
            'diagnosis',
            'content',]
