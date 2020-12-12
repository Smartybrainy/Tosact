from django.db import models


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
