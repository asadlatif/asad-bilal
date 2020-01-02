from django.shortcuts import render
from django.core.mail import BadHeaderError, send_mail
from django.http import HttpResponse
from django.core.mail import EmailMessage


def profile(request):
 if request.POST:
    To_email = request.POST.get('email', '')
    if To_email:
        try:


         # mail_subject = 'Active a sua conta.'
         # message = "message"
         #
         #
         # email = EmailMessage(
         # mail_subject, message, to=[To_email]
         #     )
         # email.send()
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


def sample_test(request):
    questions = test.objects.all()
    return render(request, 'SampleTest.html',{ "Test":questions })


def feedback(request):
    return render(request, 'feedback.html')


def lockscreen(request):
    return render(request, 'lockScreern.html')


def register(request):
    return render(request, 'register.html')


