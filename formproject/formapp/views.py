from django.shortcuts import render
from . import forms

# Create your views here.
def studentregistationview(request):
	form=forms.studentregistation()
	return render(request,'formapp/display.html',{'form':form})