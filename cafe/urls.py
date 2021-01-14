from django.urls import path
from .views import (HomeView, BlogListView, BlogDetailView, blog_likes)

app_name = 'cafe'

urlpatterns = [
    path('', HomeView.as_view(), name="home"),
    path('blog/', BlogListView.as_view(), name="blog-list-view"),
    path("blog/<slug>/", BlogDetailView.as_view(), name="blog-detail-view"),
    path('<pk>/likes/', blog_likes, name="blog-likes")
]
