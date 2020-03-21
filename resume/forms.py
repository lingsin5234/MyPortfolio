from django import forms
from .models import ContactMe
from captcha.fields import CaptchaField


class CaptchaContactForm(forms.ModelForm):

    message = forms.CharField(max_length=500, widget=forms.Textarea)
    captcha = CaptchaField(help_text="(case insensitive)")

    class Meta:
        model = ContactMe
        fields = ['name', 'email', 'message', 'captcha']
