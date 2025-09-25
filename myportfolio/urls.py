from django.contrib import admin
from django.urls import path
from portfolioapp import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.index, name='index'),
    path('about_us.html', views.about_us, name='about_us'),
    path('contacts.html', views.contacts, name='contacts'),
]
