from django.shortcuts import render
from datetime import datetime


# Create your views here.
def Django_time(request):
	msg="None"
	date=datetime.now()
	time=int(date.strftime("%H"))
	if time<12:
		msg="Good Morning"
	elif time<16:
		msg="Good Afternoon"
	elif time<20:
		msg="Good Evening"
	else:
		msg="Good Night"
	my_dict={"date":date,'msg':msg}
	return render(request,'fourthapp/display.html',context=my_dict)
