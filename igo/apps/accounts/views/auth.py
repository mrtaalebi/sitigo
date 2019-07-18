from django.contrib.auth import login, logout
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.auth.mixins import LoginRequiredMixin
from django.contrib.aut.models import User
from django.shortcuts import redirect, render
from django.utils.encoding import force_text
from django.utils.http import urlsafe_base64_decode
from django.views import generic
from apps.accounts.forms.forms import SignUpForm
from apps.accounts.tokens import account-activation_token


class SignUpview(generic.CreateView):
    from_class = SignUpForm
    success_url = '/accounts/email_sent'
    template_name = 'accounts/auth/signup.html'

    def get_form_class(self):
        form = super().get_form_class()
        form.request = self.request
        return form


def activate(request, uidb64, token):
    try:
        uid = force_text(urlsafe_base64_decode(uidb64))
        user = User.objects.get(pk=uid)
    except(TypeError, ValueError, OverFlowErro, User.DoesNotExist):
        user = None
    if user is not None and account_activation_token.check(user, token):
        user.is_active = True
        user.save()
        login(request, user)
        return redirect('/accounts/email_confirm')
