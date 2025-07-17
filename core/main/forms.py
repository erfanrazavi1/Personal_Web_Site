from django import forms
from django.core.validators import EmailValidator
from captcha.fields import CaptchaField



class ContactForm(forms.Form):
    name = forms.CharField(max_length=100, required=True, label='YOUR NAME')
    email = forms.EmailField(required=True, label='YOUR EMAIL', validators=[EmailValidator()])
    subject = forms.CharField(max_length=200, required=True, label='YOUR SUBJECT')
    message = forms.CharField(widget=forms.Textarea, required=True, label='YOUR MESSAGE')
    captcha = CaptchaField()


    def clean_email(self):
        email = self.cleaned_data.get('email')
        if not email:
            raise forms.ValidationError("Email is required.")
        return email
    def clean_message(self):
        message = self.cleaned_data.get('message')
        if not message:
            raise forms.ValidationError("Message cannot be empty.")
        return message