from django.shortcuts import render, redirect

from django.core.mail import send_mail
from django.conf import settings

from .forms import ContactInfoForm


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

    message = 'name: ' + data['name'] + '\n' \
            + 'country: ' + data['country'] + '\n' \
            + 'school_uni: ' + data['school_uni'] + '\n' \
            + 'study_grade: ' + data['study_grade'] + '\n' \
            + 'phone_number: ' + data['phone_number'] + '\n' \
            + 'email: ' + data['email'] + '\n' \
            + '\n\n\n text: \n\n\n' + data['text']

    recipient_list = ['national.igo@gmail.com']

    send_mail(subject=subject,
            message=message,
            from_email='igoiiggooiiigggooo@gmail.com',
            recipient_list=recipient_list
            )

    return redirect('contact_us/sent.html')


def sent(request):
    return render(request, 'contact_us/sent.html')

