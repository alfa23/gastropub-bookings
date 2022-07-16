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

# # https://stackoverflow.com/questions/64293242/how-to-link-django-custom-user-model-and-django-allauth-package

# from allauth.account.forms import SignupForm
# from django import forms
# from .models import User, UserReg


# class MyCustomSignupForm(SignupForm):

#     def __init__(self, *args, **kwargs):
#         super(MyCustomSignupForm, self).__init__(*args, **kwargs)
#         first_name = forms.CharField(max_length=25, label='First Name')
#         last_name = forms.CharField(max_length=25, label='Last Name')
#         contact_no = forms.CharField(max_length=25, label='Contact Number')

#     # Put in custom signup logic
#     def UserReg(self, request, user):
#         # Set the user's type from the form reponse
#         user.first_name = self.cleaned_data['first_name']
#         user.last_name = self.cleaned_data['last_name']
#         user.contact_no = self.cleaned_data['contact_no']
#         # user.email = self.cleaned_data['email']

#         # Save the user's type to their database record
#         user.save()
#         return user
