from django.db import models
from django.urls import reverse
from django.contrib.auth.models import User

LIKE_VALUE = (('Like', "Like"), ("Unlike", "Unlike"))


class ContactEnquiries(models.Model):
    name = models.CharField(max_length=25)
    email = models.EmailField()
    phone_number = models.IntegerField()
    message = models.TextField()
    granted = models.BooleanField(default=False)

    def __str__(self):
        return "%s and %s" % (self.name, self.email)

    class Meta:
        verbose_name_plural = "Contacts & Enquiries"


class Blog(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    image = models.ImageField(upload_to="blog_photos/", blank=True, null=True)
    title = models.CharField(max_length=200, unique=True)
    slug = models.SlugField(max_length=255, unique=True)
    content = models.TextField()
    date_created = models.DateTimeField(auto_now_add=True)
    liked = models.ManyToManyField(User,
                                   blank=True,
                                   default=None,
                                   related_name="likes")

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse("cafe:blog-detail-view", kwargs={"slug": self.slug})

    @property
    def likes_count(self):
        return self.liked.all().count()

    class Meta:
        verbose_name_plural = "Blog post"
        ordering = ['-date_created']


class Like(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    blog = models.ForeignKey(Blog, on_delete=models.CASCADE)
    value = models.CharField(max_length=6, choices=LIKE_VALUE, default="Like")

    def __str__(self):
        return f"{self.blog.title}"

    class Meta:
        verbose_name_plural = "Blog likes"