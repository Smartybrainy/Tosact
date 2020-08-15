from django.shortcuts import render


def home(request):
    return render(request, 'cafe/home.html')
