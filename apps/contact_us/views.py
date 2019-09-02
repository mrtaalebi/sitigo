from django.shortcuts import render, redirect
from django.utils import translation
from django.core.mail import send_mail
from django.conf import settings

from .forms import ContactInfoForm

import pycountry

def contact_us(request):
    
    if request.method == 'POST':
        form = ContactInfoForm(request.POST)
        if form.is_valid():
            print(form.cleaned_data)
            form.save()
        else:
            return render(request, 'contact_us/contact_us.html', {'form': form})
    else:
        form = ContactInfoForm()
        return render(request, 'contact_us/contact_us.html', {'form': form})

    data = form.cleaned_data

    subject = data['subject']

    message = 'Name: ' + data['name'] + '\n' \
            + 'Country: ' + pycountry.countries.get(alpha_3=data['country']).name + '\n' \
            + 'School/University: ' + data['school_uni'] + '\n' \
            + 'Study Grade: ' + data['study_grade'] + '\n' \
            + 'Phone Number: ' + data['phone_number'] + '\n' \
            + 'Email: ' + data['email'] + '\n' \
            + '\n Message: \n' + data['text']

    lang = translation.get_language()
    recp = 'national.igo@gmail.com' if lang == "fa" else 'international.igo@gmail.com'
    recipient_list = [recp]

    send_mail(subject=subject,
            message=message,
            from_email='igoiiggooiiigggooo@gmail.com',
            recipient_list=recipient_list
            )

    return sent(request)


def sent(request):
    return render(request, 'contact_us/sent.html')

