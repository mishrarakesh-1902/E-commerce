from django import forms
from .models import Feedback

# from django.contrib.auth.models import User



class FeedbackForm(forms.ModelForm):
    class Meta:
        model = Feedback
        fields = ['brand_name', 'product_name', 'name', 'email', 'rating', 'comments']
        widgets = {
            'comments': forms.Textarea(attrs={'rows': 4, 'placeholder': 'Write your feedback...'}),
        }

