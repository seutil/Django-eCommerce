from django.urls import reverse_lazy
from django.contrib.auth import views

from . import forms


class LoginView(views.LoginView):
    authentication_form = forms.LoginForm
    redirect_authenticated_user = True

    def form_valid(self, form):
        remember_me = form.cleaned_data['remember_me']
        if not remember_me:
            self.request.session.set_expiry(0)  # close session after the browser is closed
            self.request.session.modified = True
        
        return super().form_valid(form)
