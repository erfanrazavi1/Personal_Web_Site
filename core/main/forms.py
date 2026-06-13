from django import forms
from django.utils.translation import gettext as _
from captcha.fields import CaptchaField


class ContactForm(forms.Form):
    name = forms.CharField(
        max_length=100,
        required=True,
        widget=forms.TextInput(attrs={"placeholder": _("YOUR NAME")}),
    )
    email = forms.EmailField(
        required=True, widget=forms.EmailInput(attrs={"placeholder": _("YOUR EMAIL")})
    )
    subject = forms.CharField(
        max_length=200,
        required=True,
        widget=forms.TextInput(attrs={"placeholder": _("YOUR SUBJECT")}),
    )
    message = forms.CharField(
        widget=forms.Textarea(attrs={"placeholder": _("YOUR MESSAGE")}), required=True
    )
    captcha = CaptchaField()

    def clean_email(self):
        email = self.cleaned_data.get("email")
        if not email:
            raise forms.ValidationError("Email is required.")
        return email

    def clean_message(self):
        message = self.cleaned_data.get("message")
        if not message:
            raise forms.ValidationError("Message cannot be empty.")
        return message
