from django import forms
from .models import AccDetails
class Accountregistration(forms.ModelForm):
    # TODO: Define form fields here
    class Meta:
    	model=AccDetails
    	fields='__all__'
    