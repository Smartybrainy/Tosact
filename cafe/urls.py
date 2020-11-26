from django.urls import path
from .views import HomeView

app_name = 'cafe'

urlpatterns = [
    path('', HomeView.as_view(template_name='cafe/index.html'), name="home"),
]
