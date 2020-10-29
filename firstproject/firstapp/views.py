from django.shortcuts import render
from django.http import HttpResponse

# Create your views here
def Welcome_django(request):
	s1="<center> <h1 style='color:red'> Hello djanog's python world </h1></center>"
	s2="<center> <h1 style='color:blue'> Welcome to the Django Framework </h1></center>"
	s3=(s1,s2)
	return HttpResponse(s3)