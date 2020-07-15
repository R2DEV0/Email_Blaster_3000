from django.shortcuts import render, redirect
import os
import smtplib
from email.message import EmailMessage


# Main Email page #
def index(request):
    return render(request, 'main.html')


# Password instructions page #
def info(request):
    return render(request, 'info.html')


# Email blaster function #
def blast(request):
# set email and password variables from form #
    email_address = request.POST['email']
    email_password = request.POST['password']

# set contact list to be email blasted from form #
    form_contacts = request.POST['email_to']
    contacts = form_contacts.split()

# set subject and message variables from form #
    email_subject = request.POST['subject']
    email_message = request.POST['message']

# run a for loop to email each contact directly #
    for contact in contacts:
        msg = EmailMessage()
        msg['Subject'] = email_subject
        msg['From'] = email_address
        msg['To'] = contact
        msg.set_content(email_message)

# attach my resume & cover letter to the email #
        # file = request.POST['file']
        # with open(file, 'rb') as f:
        #     file_data = f.read()
        #     file_name = f.name
        # msg.add_attachment(file_data, maintype='application', subtype='octet-stream', filename=file_name)

# login to my email and send! #
        with smtplib.SMTP_SSL('smtp.gmail.com', 465) as smtp:
            smtp.login(email_address, email_password)
            smtp.send_message(msg)
    return redirect('/')
