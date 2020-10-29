from django.shortcuts import render

# Create your views here.
def India(request):
	msg="MY workplace is India"
	my_dict={'msg':msg}
	return render (request,'countryapp/display.html',context=my_dict)

def Russia(request):
	msg="MY workplace is Russia"
	my_dict={'msg':msg}
	return render (request,'countryapp/display.html',context=my_dict)
