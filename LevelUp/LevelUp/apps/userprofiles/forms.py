from django import forms
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
