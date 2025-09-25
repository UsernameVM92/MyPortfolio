from django import forms


class ContactForm(forms.Form):
    name = forms.CharField(
        max_length=100,
        label="Name",
        widget=forms.TextInput(attrs={
            'placeholder': 'Enter your Name',
            'class': 'u-border-none u-input u-input-rectangle u-radius-20'
        })
    )
    email = forms.EmailField(
        label="Email",
        widget=forms.EmailInput(attrs={
            'placeholder': 'Enter a valid email address',
            'class': 'u-border-none u-input u-input-rectangle u-radius-20'
        })
    )
    message = forms.CharField(
        label="Message",
        widget=forms.Textarea(attrs={
            'placeholder': 'Enter your message',
            'rows': 4,
            'class': 'u-border-none u-input u-input-rectangle u-radius-20'
        })
    )

