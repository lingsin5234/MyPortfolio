from django import forms
# from contact_form.forms import ContactForm
from captcha.fields import CaptchaField


class CaptchaContactForm(forms.Form):
    """
    ContactForm subclass to add captcha protection.

    """
    name = forms.CharField(max_length=30)
    email = forms.EmailField()
    message = forms.CharField(max_length=500, widget=forms.Textarea)
    captcha = CaptchaField(help_text="(case insensitive)")
