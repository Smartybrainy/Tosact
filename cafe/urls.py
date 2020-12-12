from django.urls import path
from .views import HomeView, add_contact_me

app_name = 'cafe'

urlpatterns = [
    path('', HomeView.as_view(template_name='cafe/index.html'), name="home"),
    path('contact-me', add_contact_me, name="contact-me")
]
