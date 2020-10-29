from django.shortcuts import render

# Create your views here.
def uc1(request):
	msg="JAVA & PYTHON"
	my_dict={'msg':msg}
	return render (request,'courseapp/display.html',context=my_dict)

def uc2(request):
	msg="JAVA,PYTHON & TESTING"
	my_dict={'msg':msg}
	return render (request,'courseapp/display.html',context=my_dict)

def uc3(request):
	msg="JAVA,PYTHON,TESTING & GIT"
	my_dict={'msg':msg}
	return render (request,'courseapp/display.html',context=my_dict)