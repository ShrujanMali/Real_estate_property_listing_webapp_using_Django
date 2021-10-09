from django.shortcuts import render, HttpResponse
from .models import Contact
from django.contrib import messages
import smtplib
from email.mime.text import MIMEText

def contactus(request):
    if request.method=="POST":
        name = request.POST['name']
        email = request.POST['email']
        issue = request.POST['issue']

        if name == "" or email == "" or issue=="":
            messages.error(request, "Please fill all required fields")
        else:
            contact = Contact(name=name, email=email, issue=issue)
            contact.save()
            messages.success(request, "Your message has been successfully sent")
            send_mail(name, email, issue)
    return render(request, 'contactus.html')

def aboutus(request):
    return render(request, 'aboutus.html')

def send_mail(name, email, issue):
    port = 2525
    smtp_server = 'smtp.mailtrap.io'
    login = 'e189fae0f5a3ef'
    password = '245d15d0a12a21'
    message = f"<h3>Contact us notification</h3><ul><li>Name: {name}</li><li>Email address: {email}</li><li>Description: {issue}</li>"

    sender_email = email
    receiver_email = 'PropertyFY.mailtrap.io'
    msg = MIMEText(message, 'html')
    msg['Subject'] = 'Contact us'
    msg['From'] = sender_email
    msg['To'] = receiver_email

    # Send email
    with smtplib.SMTP(smtp_server, port) as server:
        server.login(login, password)
        server.sendmail(sender_email, receiver_email, msg.as_string())    