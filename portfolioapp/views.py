from django.shortcuts import render, redirect
from django.conf import settings
from django.core.mail import send_mail
from .forms import ContactForm


def index(request):
    return render(request, 'portfolioapp/index.html')


def contacts(request):
    return render(request, 'portfolioapp/contacts.html')


def about_us(request):
    return render(request, 'portfolioapp/about_us.html')


def contact_view(request):
    success = False
    if request.method == "POST":
        form = ContactForm(request.POST)
        if form.is_valid():
            name = form.cleaned_data['name']
            email = form.cleaned_data['email']
            message = form.cleaned_data['message']

            try:
                send_mail(
                    subject=f"Нове повідомлення від {name}",
                    message=message,
                    from_email=getattr(settings, 'DEFAULT_FROM_EMAIL', 'webmaster@localhost'),
                    recipient_list=[getattr(settings, 'CONTACT_RECEIVER_EMAIL', 'your@email')],
                    fail_silently=False,
                    reply_to=[email],
                )
            except Exception as e:
                print("Email send failed:", e)

            success = True
            form = ContactForm()
    else:
        form = ContactForm()

    return render(request, "portfolioapp/contact_section.html", {"form": form, "success": success})
