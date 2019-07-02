from django.shortcuts import render

from django.core.mail import send_mail
from django.conf import settings

from .forms import ContactInfoForm


def contact_us(request):
    
    if request.method == 'POST':
        form = ContactInfoForm(request.POST)
        if form.is_valid():
            pass  # does nothing, just trigger the validation
    else:
        form = ContactInfoForm()
    return render(request, 'contact_us/contact_us.html', {'form': form})

    subject = request.data['subject']

    message = 'name: ' + request.data['name'] + '\n' \
            + 'country: ' + request.data['country'] + '\n' \
            + 'school_uni: ' + request.data['school_uni'] + '\n' \
            + 'study_grade: ' + request.data['study_grade'] + '\n' \
            + 'phone_number: ' + request.data['phone_number'] + '\n' \
            + 'email: ' + request.data['email'] + '\n' \
            + '\n\n\n text: \n\n\n' + request.data['text']

    recipient_list = [request.data['recipient']]

    return send_mail(subject, message, recipient_list)

