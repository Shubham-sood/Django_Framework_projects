from django.shortcuts import render

# Create your views here.
def uc1(request):
	msg="Java and Python"
	my_dict={'msg':msg}
	return render (request,'courseapp/display.html',context=my_dict)

def uc2(request):
	msg="Java,Python and Testing"
	my_dict={'msg':msg}
	return render (request,'courseapp/display.html',context=my_dict)