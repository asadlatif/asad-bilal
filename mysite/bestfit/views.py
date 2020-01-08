from django.shortcuts import render
from django.core.mail import BadHeaderError, send_mail
from django.http import HttpResponse
from django.core.mail import EmailMessage
from django.db import connection

def profile(request):
 if request.POST:
    To_email = request.POST.get('email', '')
    if To_email:
        try:


          send_mail("test pin","your pin for the test is 45635",'raconnectors@gmail.com', [To_email])
        except BadHeaderError:
            return HttpResponse('Invalid header found.')
        return HttpResponse('very good')
    else:
        return HttpResponse('Make sure all fields are entered and valid.')



 else:






    return render(request, 'profile.html')


def index(request):
    return render(request, 'index.html')


def profileEdit(request):
    return render(request, 'profileEdit.html')


def instructions(request):
    return render(request, 'instructions.html')


def Test(request):
    with connection.cursor() as curser:
        curser.execute('select * from besfit_questions ')
        questions=dictfetchall(curser)



    return render(request, 'Test.html',{ "questions":questions })

def dictfetchall(cursor):

    "Return all rows from a cursor as a dict"
    columns = [col[0] for col in cursor.description]
    return [
        dict(zip(columns, row))
        for row in cursor.fetchall()
    ]


def feedback(request):
    return render(request, 'feedback.html')


def lockscreen(request):
    return render(request, 'lockScreern.html')


def register(request):
    return render(request, 'register.html')


