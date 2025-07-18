from django.views.generic.edit import FormView
from django.core.mail import send_mail
from django.contrib import messages
from django.conf import settings
from django.urls import reverse_lazy
from main.forms import ContactForm


class HomeView(FormView):
    template_name = "index.html"
    form_class = ContactForm
    success_url = reverse_lazy("main:home")

    def form_valid(self, form):
        name = form.cleaned_data["name"]
        email = form.cleaned_data["email"]
        subject = form.cleaned_data["subject"]
        message = form.cleaned_data["message"]

        send_mail(
            subject=subject,
            message=f"Name: {name}\nEmail: {email}\nMessage:\n{message}",
            from_email=settings.DEFAULT_FROM_EMAIL,
            recipient_list=["erfan6235@gmail.com"],
            fail_silently=False,
        )

        messages.success(
            self.request, "Thank you for your message, we will get back to you soon!"
        )
        return super().form_valid(form)
