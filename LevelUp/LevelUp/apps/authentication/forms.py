from django import forms
from django.contrib.auth.models import User
from django.forms.utils import ErrorList

#Custom error messages
class CustomError(ErrorList):
    def as_ul(self):
        if not self:
            return ''
        return '<ul class="text-danger">%s</ul>' % ''.join(['<li>%s</li>' % e for e in self])

#Forms
class signup_form(forms.Form):
    username = forms.CharField(
        max_length=100,
        label='Username',
        widget=forms.TextInput(
            attrs={'class':'form-control', 'placeholder':'Username'}
        )
    )
    email = forms.EmailField(
        max_length=100,
        label='Email',
        widget=forms.EmailInput(
            attrs={'class':'form-control', 'placeholder':'Email'}
        )
    )
    password = forms.CharField(
        max_length=100,
        label='Password',
        widget=forms.PasswordInput(
            attrs={'class':'form-control', 'placeholder':'Password'}
        )
    )

    def clean_username(self):
        username = self.cleaned_data['username']

        if User.objects.filter(username=username).exists():
            raise forms.ValidationError(f"Username {username} is already in use!")
        return username

    def clean_email(self):
        email = self.cleaned_data['email']

        if User.objects.filter(email=email).exists():
            raise forms.ValidationError(f"Email {email} is already in use!")
        return email

class login_form(forms.Form):
    username = forms.CharField(
        max_length=100,
        label='Username',
        widget=forms.TextInput(
            attrs={'class':'form-control', 'placeholder':'Username'}
        )
    )
    password = forms.CharField(
        max_length=100,
        label='Password',
        widget=forms.PasswordInput(
            attrs={'class':'form-control', 'placeholder':'Password'}
        )
    )
