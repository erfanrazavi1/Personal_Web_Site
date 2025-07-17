from django.shortcuts import render, redirect
from django.http import HttpResponse
from main.forms import ContactForm
from django.views.generic import TemplateView
from django.contrib import messages
from captcha.helpers import captcha_image_url
from captcha.models import CaptchaStore

# Create your views here.

def home(request):
    new_key = CaptchaStore.generate_key()
    image_url = captcha_image_url(new_key)
    if request.method == "POST":
        form = ContactForm(request.POST)
        if form.is_valid():
            name = form.cleaned_data['name']
            email = form.cleaned_data['email']
            subject = form.cleaned_data['subject']
            message = form.cleaned_data['message']
            human = True
            messages.success(request, 'Thank you for your message, we will get back to you soon!')
            return redirect('main:home')
    else:
        form = ContactForm()
    return render(request, 'index.html', {
        'form': form,
        'captcha_key': new_key,
        'captcha_image_url': image_url,
        })


