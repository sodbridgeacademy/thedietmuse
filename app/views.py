from django.shortcuts import render, redirect
from django.core.mail import BadHeaderError, send_mail, EmailMessage
from django.conf import settings
from .models import *
from django.views.generic import CreateView, ListView, DetailView

# Create your views here.
def index(request):
    events = Event.objects.all()
    specials = Specials.objects.all()
    food_menu = Food.objects.all()
    gallery = Gallery.objects.all()
    testimonials = Testimonial.objects.all()
    
    if request.method == 'POST':
        fullname = request.POST['name']
        contact_email = request.POST['email']
        subject = request.POST['subject']
        message = request.POST['message']
        print('message from contact form:', message)
    
        # Extra email details
        #subject = 'A New Message From SeamlessBuy Store'
        contact_message = f'The Diet Muse; New Message, \n\n' \
                f'You have a message from {fullname} with details below. \n\n' \
                f'contact email: {contact_email} \n\n' \
                f'Message: {message}.'
        email_msg = EmailMessage(
            subject=subject, body=contact_message, 
            from_email=contact_email,
            to=[settings.EMAIL_HOST_USER],
            headers={'Reply-To': contact_email})
        email_msg.send()
        messages.success(request, f'Thank you for contacting us! We\'ll get back to you soon.')
        print('Mesage delivered!!!')
        return redirect('success')
    context = {
        'events':events,
        'specials':specials,
        'food_menu':food_menu,
        'gallery':gallery,
        'testimonials':testimonials
    }
    return render(request, 'app/index.html', context)

def contact(request):
    # Validate contact form 
    if request.method == 'POST':
        fullname = request.POST['name']
        print('fullname from contact: ', fullname)
        contact_email = request.POST['email']
        subject = request.POST['subject']
        message = request.POST['message']

        print('message from contact form:', message)
    
        # Extra email details
        #subject = 'A New Message From SeamlessBuy Store'
        contact_message = f'The Diet Muse; New Message, \n\n' \
                f'You have a message from {fullname} with details below. \n\n' \
                f'contact email: {contact_email} \n\n' \
                f'Message: {message}.'
        email_msg = EmailMessage(
            subject=subject, body=contact_message, 
            from_email=contact_email,
            to=[settings.EMAIL_HOST_USER],
            headers={'Reply-To': contact_email})
        email_msg.send()
        messages.success(request, f'Thank you for contacting us! We\'ll get back to you soon.')
        print('Mesage delivered!!!')
        return redirect('success')
    return render(request, 'app/index.html')
