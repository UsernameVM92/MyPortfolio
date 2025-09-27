from django.shortcuts import render, redirect
from .forms import MessageForm
from .models import Contact, Project, Skill
from django.core.mail import send_mail
from django.shortcuts import render, redirect


def index(request):
    success = False

    if request.method == "POST":
        form = MessageForm(request.POST)
        if form.is_valid():
            message = form.save()

            send_mail(
                subject=f"Нове повідомлення від {message.name}",
                message=f"Ім'я: {message.name}\nEmail: {message.email}\n\n{message.message}",
                from_email=message.email,
                recipient_list=["vovamazur677@gmail.com"],
            )

            success = True
            form = MessageForm()

    else:
        form = MessageForm()

    contact = Contact.objects.first()
    projects = Project.objects.all()
    skills = Skill.objects.all()

    return render(request, "portfolioapp/index.html", {
        "form": form,
        "success": success,
        "contact": contact,
        "projects": projects,
        "skills": skills,
    })

