from django import forms
from django.contrib.auth.models import User
from django.forms.utils import ErrorList
from django.forms import BaseFormSet
import datetime

#Custom error messages
class CustomError(ErrorList):
    def as_ul(self):
        if not self:
            return ''
        return '<ul class="text-danger">%s</ul>' % ''.join(['<li>%s</li>' % e for e in self])

#Custom formset
class RequiredFormSet(BaseFormSet):
    def __init__(self, *args, **kwargs):
        super(RequiredFormSet, self).__init__(*args, **kwargs)
        for form in self.forms:
            form.empty_permitted = False

#Forms
class workout_form(forms.Form):
    date = forms.DateField(
        initial=datetime.date.today,
        label='Date',
        widget=forms.SelectDateWidget(
            attrs={'class':'form-control'}
        )
    )
    num_exercises = forms.IntegerField(
        max_value=100,
        min_value=1,
        label='Number of Exercises',
        widget=forms.NumberInput(
            attrs={'class':'form-control'}
        )
    )

class exercise_form(forms.Form):
    name = forms.CharField(
        max_length=100,
        label='Name',
        widget=forms.TextInput(
            attrs={'class':'form-control', 'required':''}
        )
    )
    sets = forms.IntegerField(
        max_value=100,
        min_value=1,
        label='Sets',
        widget=forms.NumberInput(
            attrs={'class':'form-control', 'required':''}
        )
    )
    reps = forms.IntegerField(
        max_value=100,
        min_value=1,
        label='Reps',
        widget=forms.NumberInput(
            attrs={'class':'form-control', 'required':''}
        )
    )
    weight = forms.IntegerField(
        max_value=10000,
        min_value=0,
        label='Weight',
        widget=forms.NumberInput(
            attrs={'class':'form-control', 'required':''}
        )
    )

class edit_profile_form(forms.Form):
    username = forms.CharField(
        max_length=100,
        label='Username',
        required=False,
        widget=forms.TextInput(
            attrs={'class':'form-control borderless text-center p-0 shadow-none', 'style':'outline: none !important; background: none; font-size: 30px;'}
        )
    )
    first_name = forms.CharField(
        max_length=100,
        label='First Name',
        required=False,
        widget=forms.TextInput(
            attrs={'class':'form-control borderless text-center p-0 shadow-none', 'style':'outline: none !important; background: none; font-size: 20px;'}
        )
    )
    last_name = forms.CharField(
        max_length=100,
        label='Last Name',
        required=False,
        widget=forms.TextInput(
            attrs={'class':'form-control borderless text-center p-0 shadow-none', 'style':'outline: none !important; background: none; font-size: 20px;'}
        )
    )

    def __init__(self, username_placeholder, first_name_placeholder, last_name_placeholder, *args, **kwargs):
        super(edit_profile_form, self).__init__(*args, **kwargs)
        self.fields["username"].widget.attrs['placeholder'] = "username" if username_placeholder == "" else username_placeholder
        self.fields["first_name"].widget.attrs['placeholder'] = "first name" if first_name_placeholder == "" else first_name_placeholder
        self.fields["last_name"].widget.attrs['placeholder'] = "last name" if last_name_placeholder == "" else last_name_placeholder

    def clean_username(self):
        username = self.cleaned_data['username']

        if username == "":
            return username

        if User.objects.filter(username=username).exists():
            raise forms.ValidationError(f"Username {username} is already in use!")
        return username
