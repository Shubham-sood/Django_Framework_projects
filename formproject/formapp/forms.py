from django import forms
class studentregistation(forms.Form):
    # TODO: Define form fields here
    Name = forms.CharField()
    MARKS = forms.IntegerField()