from django.shortcuts import render
from . import forms
from django.http import HttpResponse

# Create your views here.
def accreq(request):
	form=forms.Accountregistration()
	if request.method=='POST':
		form=forms.Accountregistration(request.POST)
		if form.is_valid():
			form.save()
			print("DATA get inserted into the database sucessfully")
			return success(request)
	return render(request,'bankformapp/display.html',{'form':form})
def success(request):
	s1="<center><h1>Successfully uploaded</h1</center>"
	return HttpResponse(s1)