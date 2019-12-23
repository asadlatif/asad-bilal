from django.shortcuts import render


def profile(request):
    return render(request, 'profile.html')


def index(request):
    return render(request, 'profile.html')


def profileEdit(request):
    return render(request, 'profileEdit.html')
