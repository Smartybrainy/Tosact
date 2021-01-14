from django.shortcuts import render, redirect
from django.views.generic import View, ListView, DetailView, TemplateView
from django.core.exceptions import ObjectDoesNotExist
from django.contrib import messages
from django.http import JsonResponse
from django.forms.models import model_to_dict
from django.contrib.auth.decorators import login_required

from .models import ContactEnquiries, Blog, Like
from .forms import ContactEnquiriesForm


class HomeView(View):
    def get(self, *args, **kwargs):
        c_form = ContactEnquiriesForm()
        context = {"form": c_form}
        return render(self.request, 'cafe/index.html', context)

    def post(self, *args, **kwargs):
        c_form = ContactEnquiriesForm(self.request.POST or None)
        if c_form.is_valid():
            name = c_form.cleaned_data.get("name")
            email = c_form.cleaned_data.get("email")
            phone_number = c_form.cleaned_data.get("phone_number")
            message = c_form.cleaned_data.get("message")
            # create new contact
            new_contact = ContactEnquiries(name=name,
                                           email=email,
                                           phone_number=phone_number,
                                           message=message)
            new_contact.save()
            return JsonResponse({"contact": model_to_dict(new_contact)},
                                status=200)
        messages.warning(self.request, "Message failed!")
        c_form = ContactEnquiriesForm()
        return redirect('/')


class BlogListView(ListView):
    model = Blog
    paginate_by = 15


class BlogDetailView(DetailView):
    model = Blog


@login_required
def blog_likes(request, *args, **kwargs):
    user = request.user
    if request.method == "POST":
        blog_id = request.POST.get('blog_id')
        blog_obj = Blog.objects.get(id=blog_id)

        if user in blog_obj.liked.all():
            blog_obj.liked.remove(user)
        else:
            blog_obj.liked.add(user)

        like, created = Like.objects.get_or_create(user=user, blog_id=blog_id)
        if not created:
            if like.value == "Like":
                like.value = "Unlike"
            else:
                like.value = "Like"
        like.save()
        blog_obj.save()

        data = {"value": like.value, "likes": blog_obj.liked.all().count()}
        return JsonResponse(data, safe=False)

    return redirect("cafe:blog-detail-view", blog_obj.slug)
