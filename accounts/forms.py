from django import forms
from django.contrib.auth import forms as auth_forms

from . import models


class LoginForm(auth_forms.AuthenticationForm):
    remember_me = forms.BooleanField(initial=True, required=False)


class SignUpForm(auth_forms.UserCreationForm):
    class Meta(auth_forms.UserCreationForm.Meta):
        model = models.User
        fields = auth_forms.UserCreationForm.Meta.fields + ('email',)


class UserForm(forms.ModelForm):
    class Meta:
        model = models.User
        fields = ('avatar', 'username', 'email', 'first_name', 'last_name',)
