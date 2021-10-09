from django.urls import path
from . import views

urlpatterns = [
    path('', views.contactus, name="contactus"),
    path('aboutus.html', views.aboutus, name='aboutus'),
]