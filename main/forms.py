from django import forms
from main.models import Registration, Testimonial

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


class TestimonialForm(forms.ModelForm):
    class Meta:
        model = Testimonial
        fields = ['name', 'role', 'comment', 'rating']
        widgets = {
            'name': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Ismingiz'
            }),
            'role': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Kasbingiz (masalan: Talaba, Tadbirkor)'
            }),
            'comment': forms.Textarea(attrs={
                'class': 'form-control',
                'placeholder': 'Fikringizni yozing...',
                'rows': 4
            }),
            'rating': forms.HiddenInput(),
        }