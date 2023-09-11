from django.urls import reverse_lazy, reverse
from django.shortcuts import redirect
from django.views import generic as views
from django.views.generic import edit
from django.contrib.auth import views as auth_views
from django.contrib.auth import mixins as auth_mixins
from django.contrib.auth import get_user_model

from . import models
from . import forms


class LoginView(auth_views.LoginView):
    authentication_form = forms.LoginForm
    redirect_authenticated_user = True

    def form_valid(self, form):
        remember_me = form.cleaned_data['remember_me']
        if not remember_me:
            self.request.session.set_expiry(0)  # close session after the browser is closed
            self.request.session.modified = True
        
        return super().form_valid(form)


class SingUpView(views.CreateView):
    form_class = forms.SignUpForm
    template_name = 'registration/signup.html'
    success_url = reverse_lazy('account_login')


class LogoutView(auth_views.LogoutView):
    ...


class UserView(auth_mixins.LoginRequiredMixin, auth_mixins.UserPassesTestMixin, views.UpdateView):
    model = models.User
    form_class = forms.UserForm

    def get_initial(self):
        return {
            'avatar': self.request.user.avatar,
            'username': self.request.user.get_username(),
            'email': self.request.user.email,
            'first_name': self.request.user.first_name,
            'last_name': self.request.user.last_name,
        }

    def test_func(self):
        return self.request.user == get_user_model().objects.get(pk=self.kwargs['pk'])

    def handle_no_permission(self):
        return redirect(reverse('home'))
