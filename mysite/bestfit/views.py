from django.shortcuts import render
from django.core.mail import BadHeaderError, send_mail
from django.http import HttpResponse
from django.core.mail import EmailMessage
from .models import Registerations, ProfileEdit
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import redirect


@login_required()
def profile(request):
    return render(request, 'profile.html')


def index(request):
    if request.POST:
        user_e = request.POST.get("email")
        user_p = request.POST.get("password")
        user = Registerations()
        if user.email == user_e and user.password == user_p:
            return render(request, 'profile.html')
        else:
            return redirect('register')
    else:
        return render(request, 'index.html')
# if request.POST:
#     To_email = request.POST.get('email', '')
#     if To_email:
#         try:
#             send_mail("test pin", "your pin for the test is 45635", 'raconnectors@gmail.com', [To_email])
#         except BadHeaderError:
#             return HttpResponse('Invalid header found.')
#         return HttpResponse('very good')
#     else:
#         return HttpResponse('Make sure all fields are entered and valid.')
# else:


# @login_required()
def sample_test(request):
    return render(request, 'SampleTest.html')


def instructions(request):
    return render(request, 'instructions.html')


def feedback(request):
    return render(request, 'feedback.html')


def lockscreen(request):
    return render(request, 'lockScreern.html')


def register(request):
    if request.POST:
        user_reg = Registerations()
        user_reg.first_name = request.POST.get("first_name")
        user_reg.last_name = request.POST.get("last_name")
        user_reg.mobile = request.POST.get("mobile")
        user_reg.email = request.POST.get("email")
        user_reg.password = request.POST.get("password")
        user_reg.education = request.POST.get("education")
        user_reg.save()
    return render(request, 'register.html')

@login_required
def proifleEdit(request):
    if request.POST:
        profileedit = ProfileEdit()
        profileedit.DOB = request.POST.get("DOB")
        profileedit.address = request.POST.get("address")
        profileedit.city = request.POST.get("city")
        profileedit.university = request.POST.get("university")
        profileedit.gender = request.POST.get("gender")
        profileedit.interest = request.POST.get("interest")
        profileedit.occupation = request.POST.get("occupation")
        profileedit.about = request.POST.get("about")
        profileedit.save()
    return render(request, 'profileEdit.html')
