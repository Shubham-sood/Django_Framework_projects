from django.shortcuts import render
from datetime import datetime
from django.http import HttpResponse

# Create your views here.
def Django_greet(request):
	msg="Good Morning"
	date= datetime.now()
	my_dict={'msg':msg,'date':date}
	return render(request,'Thirdapp/display.html',context=my_dict)