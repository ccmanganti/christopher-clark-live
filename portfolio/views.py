from django.shortcuts import render
from .models import Project
from django.views.decorators.csrf import csrf_exempt
from django.core.mail import send_mail
# Create your views here.

context = {
        'projects': Project.objects.all()   
    }

def index(request):
    return render(request, 'portfolio/index.html', context)

def projects(request):
    return render(request, 'portfolio/projects.html', context)

def blog(request):
    return render(request, 'portfolio/blog.html')

@csrf_exempt
def contact(request):

    if request.method == "POST":
        firstName = request.POST['firstName']
        lastName = request.POST['lastName']
        messageEmail = request.POST['message-email']
        messageSubject = request.POST['message-subject']
        message = request.POST['message']

        # Sends an email
        send_mail('Message from ' + firstName +' ' + lastName + ' ' + '| ' + messageSubject, 
        message + ' ' + '|' + ' Mail from Personal Website' + ' ' + messageEmail, 
        messageEmail, 
        ['cpe.christopherclarkcmanganti@gmail.com'],)

        return render(request, 'portfolio/contact.html', {'firstName': 'Thank you for the message ' + firstName + '!'})
    else:
        return render(request, 'portfolio/contact.html', {})
