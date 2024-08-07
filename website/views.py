from django.contrib import messages
from django.shortcuts import render, redirect
from .forms import ContactForm
from django.core.mail import BadHeaderError, send_mail
from django.http import HttpResponse


# Create your views here.
def home(request):
    return render(request,'home.html')

def service(request):
    return render(request, 'service.html')

def about(request):
    return render(request, 'about.html')

def contacts(request):
    if request.method == 'POST':
        print('In post')
        form = ContactForm(request.POST)
        if form.is_valid():
            print('form valid')
            subject = form.cleaned_data.get('topic')
            email_address = form.cleaned_data.get('email')
            client_name = form.cleaned_data.get('name')
            message = form.cleaned_data.get('message')
            company = form.cleaned_data.get('company')
            phone = form.cleaned_data.get('phone_number')
            full_message = f"""
            ________________________
            A message has been received from your website www.macronsynergy.co.zw.
            Here are the client details below 
            Client name: {client_name}
            Client company(if any): {company}, 
            contact number: {phone}
            email address: {email_address}
            ________________________
            Below is the message from the client
            ________________________


            {message}
            """
            try:
                print('sending email...')
                send_mail(subject=subject,
                          message = full_message,
                          from_email="enquiry@macronsynergy.co.zw",
                          recipient_list=["info@macronsynergy.co.zw"],
                          )
                messages.success(request, 'Thank you, we have received your message. We will get back to you soon. ')
                print('done')
            except BadHeaderError:
                return HttpResponse("Invalid header found")
            return redirect('website:contacts')
        else:
            cxt = {'form': form}
            return render(request, 'contacts.html', cxt)  # Redirect to a success page
    else:
        form = ContactForm()
    return render(request, 'contacts.html', {'form': form})

def careers(request):
    return render(request, 'careers.html')


