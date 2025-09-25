from django.contrib import admin
from .models import Profile, Skill, Experience, Contact, Project


class SkillInline(admin.TabularInline):
    model = Skill
    extra = 1


class ExperienceInline(admin.TabularInline):
    model = Experience
    extra = 1


class ContactInline(admin.StackedInline):
    model = Contact
    extra = 0


class ProfileAdmin(admin.ModelAdmin):
    inlines = [SkillInline, ExperienceInline, ContactInline]


admin.site.register(Profile)
admin.site.register(Skill)
admin.site.register(Experience)
admin.site.register(Contact)
admin.site.register(Project)
