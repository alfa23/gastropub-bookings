# Create custom AllAuth SignupForm to collect additional user data (first
# name, last name, contact_no) - copied & expanded-upon code sourced from:
# https://www.geeksforgeeks.org/python-extending-and-customizing-django-allauth/

from allauth.account.forms import SignupForm
from django import forms
from .models import User, UserReg


class MyCustomSignupForm(SignupForm):
    first_name = forms.CharField(max_length=25, label='First Name')
    last_name = forms.CharField(max_length=25, label='Last Name')
    contact_no = forms.CharField(max_length=30, label='Contact Number')

    def save(self, request):
        user = super(MyCustomSignupForm, self).save(request)
        user.first_name = self.cleaned_data['first_name']
        user.last_name = self.cleaned_data['last_name']
        user.contact_no = self.cleaned_data['contact_no']
        user.save()
        return user

