from django.shortcuts import render, redirect
from django.http import HttpResponse
from main.forms import ContactForm
from django.views.generic import TemplateView
from django.contrib import messages

# Create your views here.

def home(request):
    if request.method == "POST":
        form = ContactForm(request.POST)
        if form.is_valid():
            name = form.cleaned_data['name']
            email = form.cleaned_data['email']
            subject = form.cleaned_data['subject']
            message = form.cleaned_data['message']


            messages.success(request, 'Thank you for your message, we will get back to you soon!')
            return redirect('main:home')
    else:
        form = ContactForm()
    return render(request, 'index.html', {'form': form})



    template_name = 'index.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['form'] = ContactForm()
        return context
    

    