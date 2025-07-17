from django.shortcuts import render, redirect
from django.http import HttpResponse
from main.forms import ContactForm
from django.views.generic import TemplateView
from django.contrib import messages
from django.core.mail import send_mail
from django.conf import settings

# Create your views here.

def home(request):
    if request.method == "POST":
        form = ContactForm(request.POST)
        if form.is_valid():
            name = form.cleaned_data['name']
            email = form.cleaned_data['email']
            subject = form.cleaned_data['subject']
            message = form.cleaned_data['message']
            human = True
            send_mail(
                subject=subject,
                message=f"Name: {name}\nEmail: {email}\nMessage:\n{message}",
                from_email=settings.DEFAULT_FROM_EMAIL,
                recipient_list=['erfan6235@gmail.com'],
                fail_silently=False,
            )
            messages.success(request, 'Thank you for your message, we will get back to you soon!')
            return redirect('main:home')
    else:
        form = ContactForm()
    return render(request, 'index.html', {'form': form})



