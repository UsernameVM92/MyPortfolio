from django import forms
from .models import Message


class MessageForm(forms.ModelForm):
    class Meta:
        model = Message
        fields = ['name', 'email', 'message']
        widgets = {
            'name': forms.TextInput(attrs={
                'class': 'u-border-none u-input u-input-rectangle u-radius-20',
                'placeholder': 'Enter your name'
            }),
            'email': forms.EmailInput(attrs={
                'class': 'u-border-none u-input u-input-rectangle u-radius-20',
                'placeholder': 'Enter a valid email address'
            }),
            'message': forms.Textarea(attrs={
                'class': 'u-border-none u-input u-input-rectangle u-radius-20',
                'rows': 4,
                'placeholder': 'Enter your message'
            }),
        }
