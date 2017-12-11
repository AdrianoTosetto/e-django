from django import forms
from home.models import AppUser


class AppUserForm(forms.Form):
    first_name = forms.CharField(required=True)
    upass      = forms.CharField(required=True)
    confirm_pass = forms.CharField(required=True)
    image = forms.ImageField(required=True)


class AppUserLoginForm(forms.Form):
    first_name   = forms.CharField(required=True)
    upass        = forms.CharField(required=True)
		