
from django import forms
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm, UsernameField
from django.contrib.auth.models import User
from django.forms import widgets
from django.utils.translation import gettext, gettext_lazy as _


class SignUpFrom(UserCreationForm):
    password1 = forms.CharField(
        label='Password', widget=forms.PasswordInput(attrs={'class': 'form-control '}))
    password2 = forms.CharField(
        label='Confirm_password(again)', widget=forms.PasswordInput(attrs={'class': 'form-control '}))
    class Meta:
        model = User
        fields = ['username', 'email', 'first_name', 'last_name']
        labels = {'first_name': 'First Name',
                  'last_name': 'Last Name', 'email': 'Email'}
        widgets = {'username': forms.TextInput(attrs={'class': 'form-control  '}),
                   'first_name': forms.TextInput(attrs={'class': 'form-control '}),
                   'last_name': forms.TextInput(attrs={'class': 'form-control '}),
                   'email': forms.EmailInput(attrs={'class': 'form-control '}),
                   }


class LoginFrom(AuthenticationForm):
    username = UsernameField(widget=forms.TextInput(attrs={'class':'form-control'}))
    password = forms.CharField(label=_("password"), strip=False, widget=forms.PasswordInput(
        attrs={'autocomplete': 'current-password', 'class': 'form-control'}))