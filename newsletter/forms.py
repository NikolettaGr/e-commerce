"""Forms for email notifications."""
from django import forms
from .models import EmailNewsNotification

class EmailNewsNotificationForm(forms.ModelForm):
    """Form for email news notifications."""
    class Meta:
        model = EmailNewsNotification
        fields = ['email_name']

        widgets = {
            'email_name': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Add email name',
            }),
        }

        labels = {
            'email_name': 'Email Name',
        }
