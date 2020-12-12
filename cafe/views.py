from django.shortcuts import render, redirect
from django.views.generic.base import TemplateView
from django.contrib import messages
from .models import ContactEnquiries


class HomeView(TemplateView):
    pass


def add_contact_me(request):
    if request.method == 'POST':
        name = request.POST['name']
        email = request.POST['email']
        phone = request.POST['phone']
        message = request.POST['message']
        created = ContactEnquiries.objects.create(name=name,
                                                  email=email,
                                                  phone_number=phone,
                                                  message=message)
        created.save()
        messages.info(request, "Message sent")
        return redirect('cafe:home')
    else:
        messages.warning(request, "Message not sent!")
        return redirect('cafe:home')
