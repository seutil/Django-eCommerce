from django import forms
from django.contrib.auth import forms as auth_forms


class LoginForm(auth_forms.AuthenticationForm):
    remember_me = forms.BooleanField(initial=True, required=False)
