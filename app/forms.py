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


# Form validation tips
# Use clean_<field> for field-level validation
# Use clean() for cross-field validation

# Use ModelForm for forms tied to models
# Always set Meta class with model and fields

# Widget customization
# Use widgets={'field': forms.TextInput(attrs={'class': 'form-control'})}
