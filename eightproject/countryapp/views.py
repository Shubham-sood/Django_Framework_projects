from django.shortcuts import render

# Create your views here.
def India(request):
	msg="IAM IN INDIA AND WORKING AS A PYTHON DEVELOPER"
	my_dict={'msg':msg}
	return render (request,'countryapp/display.html',context=my_dict)

def USA(request):
	msg="IAM IN USA AND WORKING AS A PYTHON DEVELOPER"
	my_dict={'msg':msg}
	return render (request,'countryapp/display.html',context=my_dict)
