from django.db import models


class Profile(models.Model):
    name = models.CharField(max_length=100)
    position = models.CharField(max_length=150)
    about = models.TextField(default="", blank=True)
    education = models.CharField(max_length=200, blank=True)

    def __str__(self):
        return self.name


class Skill(models.Model):
    CATEGORY_CHOICES = [
        ("web", "Web Development"),
        ("backend", "Backend Development"),
        ("frontend", "Frontend Development"),
        ("data", "Data Science / Analytics"),
        ("ml_ai", "Machine Learning / AI"),
        ("devops", "DevOps / Cloud"),
        ("automation", "Automation / Scripting"),
        ("other", "Other"),
    ]

    LEVEL_CHOICES = [
        ("beginner", "Beginner"),
        ("intermediate", "Intermediate"),
        ("advanced", "Advanced"),
        ("expert", "Expert"),
    ]

    profile = models.ForeignKey(Profile, on_delete=models.CASCADE, related_name="skills")
    name = models.CharField(max_length=50)
    category = models.CharField(max_length=50, choices=CATEGORY_CHOICES, default="other")
    level = models.CharField(max_length=20, choices=LEVEL_CHOICES, default="intermediate")
    years_of_experience = models.PositiveIntegerField(default=0)
    description = models.TextField(blank=True, help_text="Деталі про використання цього скілу в проектах")

    def __str__(self):
        return f"{self.name} ({self.level})"


class Experience(models.Model):
    profile = models.ForeignKey(Profile, on_delete=models.CASCADE, related_name="experience")
    company = models.CharField(max_length=100)
    role = models.CharField(max_length=100)
    years = models.CharField(max_length=50)
    description = models.TextField(blank=True, help_text="Короткий опис досягнень та відповідальностей")

    def __str__(self):
        return f"{self.company} — {self.role}"


class Contact(models.Model):
    profile = models.OneToOneField(Profile, on_delete=models.CASCADE, related_name="contacts")
    email = models.EmailField()
    phone = models.CharField(max_length=20, blank=True, null=True)
    github = models.URLField(blank=True, null=True)
    portfolio_site = models.URLField(blank=True, null=True)

    def __str__(self):
        return self.email


class Project(models.Model):
    profile = models.ForeignKey(Profile, on_delete=models.CASCADE, related_name="projects")
    title = models.CharField(max_length=200)
    description = models.TextField()
    tech_stack = models.CharField(max_length=200, blank=True, help_text="Наприклад: Django, React, PostgreSQL")
    link = models.URLField(blank=True, null=True)
    github_link = models.URLField(blank=True, null=True)
    image = models.ImageField(upload_to="projects/", blank=True, null=True)

    def __str__(self):
        return self.title


class Message(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    message = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Message from {self.name}"
