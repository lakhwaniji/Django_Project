from django.shortcuts import render
from .forms import ApplicationForms
from .models import Form
from django.core.mail import EmailMessage
from django.contrib import messages

def index(request):
    if request.method == "POST":
        form = ApplicationForms(request.POST)
        if form.is_valid():
            first = form.cleaned_data["first_name"]
            last_name = form.cleaned_data["last_name"]
            email = form.cleaned_data["email"]
            occupation = form.cleaned_data["occupation"]

            print(form.cleaned_data)
            Form.objects.create(first=first, last_name=last_name, email=email, occupation=occupation,
                                date=date)

            '''message_body=f"Your form has been submitted Successfully \nThank you {first_name} {last_name}"
            email_message=EmailMessage("Form Submission Confirmation",message_body,to=[email])
            email_message.send()'''

            messages.success(request,"Form submitted successfully")
    return render(request, 'index.html')

def about(request):
    return render(request,'about.html')