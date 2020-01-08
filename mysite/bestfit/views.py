from django.shortcuts import render
from django.core.mail import BadHeaderError, send_mail
from django.http import HttpResponse
from django.core.mail import EmailMessage

from .models import Registerations, ProfileEdit
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import redirect
from django.db import connection

from django.db import connection

# def profile(request):
#  if request.POST:
#     To_email = request.POST.get('email', '')
#     if To_email:
#         try:
#
#
#           send_mail("test pin","your pin for the test is 45635",'raconnectors@gmail.com', [To_email])
#         except BadHeaderError:
#             return HttpResponse('Invalid header found.')
#         return HttpResponse('very good')
#     else:
#         return HttpResponse('Make sure all fields are entered and valid.')
#
#
#
#  else:
#      return render(request, 'profile.html')

@login_required()
def profile(request):
    return render(request, 'profile.html')


def index(request):
    if request.POST:
        user_e = request.POST.get("email")
        user_p = request.POST.get("password")
        with connection.cursor() as curser:
            curser.execute("select * from bestfit_registerations where email='"+user_e+"' and password ='"+user_p+"'")
            print(curser.execute("select * from bestfit_registerations where email='"+user_e+"' and password ='"+user_p+"'"))
            if curser:
                return render(request, "profile.html")
            else:
                return render(request, "index.html")
    # else:
    #     return render(request, 'index.html')
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


def instructions(request):
    return render(request, 'instructions.html')

@login_required()
def Test(request):
    with connection.cursor() as curser:
        curser.execute('select * from besfit_questions ')
        questions=dictfetchall(curser)
    return render(request, 'Test.html', {"questions": questions})


def dictfetchall(cursor):

    "Return all rows from a cursor as a dict"
    columns = [col[0] for col in cursor.description]
    return [
        dict(zip(columns, row))
        for row in cursor.fetchall()
    ]


@login_required()
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
        To_email = request.POST.get('email', '')
        if To_email:
            try:
                send_mail("test pin", "your pin for the test is 45635", 'raconnectors@gmail.com', [To_email])
            except BadHeaderError:
                return HttpResponse('Invalid header found.')

        else:

           return render(request,  'registration.html')

        return  redirect("index.html")
    else:
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
