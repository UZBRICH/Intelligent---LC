from django import forms
from main.models import Registration

class RegistrationForm(forms.ModelForm):
    class Meta:
        model = Registration
        fields = ['name', 'phone']
        widgets = {
            'name': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Ismingiz'
            }),
            'phone': forms.TextInput(attrs={
            'class': 'form-control',
            'placeholder': 'Telefon raqamingiz (Boglanish uchun)',
            'type': 'tel',
            'pattern': '[0-9+\\s\\-]{7,15}',
            'title': "Faqat raqamlar kiriting",
            'oninput': 'this.value = this.value.replace(/[^0-9+\\s\\-]/g, "")',
        })
        }