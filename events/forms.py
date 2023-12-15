from django import forms
from .models import Registration, Feedback


class RegistrationForm(forms.ModelForm):
    class Meta:
        model = Registration
        fields = ['name', 'email', 'phone_number',
                  'current_qualification', 'unique_id']
        widgets = {
            'name': forms.TextInput(attrs={'placeholder': 'Name'}),
            'email': forms.EmailInput(attrs={'placeholder': 'Email'}),
            'phone_number': forms.TextInput(attrs={'placeholder': 'Phone Number'}),
            'current_qualification': forms.TextInput(attrs={'placeholder': 'Current Qualification'}),
            'unique_id': forms.TextInput(attrs={'placeholder': 'Unique ID (optional)'}),
        }
        labels = {
            'name': '',
            'email': '',
            'phone_number': '',
            'current_qualification': '',
            'unique_id': '',
        }


class FeedbackForm(forms.ModelForm):
    class Meta:
        model = Feedback
        fields = ['name', 'email', 'phone_number',
                  'current_qualification', 'unique_id', 'rating', 'text']
        widgets = {
            'name': forms.TextInput(attrs={'placeholder': 'Name'}),
            'email': forms.EmailInput(attrs={'placeholder': 'Email'}),
            'phone_number': forms.TextInput(attrs={'placeholder': 'Phone Number'}),
            'current_qualification': forms.TextInput(attrs={'placeholder': 'Current Qualification'}),
            'unique_id': forms.TextInput(attrs={'placeholder': 'Unique ID (optional)'}),
            'rating': forms.NumberInput(attrs={'placeholder': 'Rating (1-5)'}),
            'text': forms.Textarea(attrs={'placeholder': 'Feedback (optional)'}),
        }
        labels = {
            'name': '',
            'email': '',
            'phone_number': '',
            'current_qualification': '',
            'unique_id': '',
            'rating': '',
            'text': '',
        }
