from django.shortcuts import render, redirect
from django.contrib import messages
from .models import Contact

def contact(request):
  if request.method == 'POST':
    name = request.POST['name']
    email = request.POST['email']
    phone = request.POST['phone']
    subject = request.POST['subject']
    message = request.POST['message']
    print()
    contact = Contact( name=name, email=email, phone=phone, subject=subject, message=message )
    contact.save()
    messages.success(request, 'Submitted Successfully')
    
    return redirect('index')
   

