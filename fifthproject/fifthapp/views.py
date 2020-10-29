from django.shortcuts import render
from datetime import datetime

# Create your views here.
def Greet_color_picture(request):
	date=datetime.now()
	time=int(date.strftime("%H"))
	msg="None"
	if time<12:
		msg="Good Morning"
	elif time<16:
		msg="Good Afternoon"
	elif time<20:
		msg="Good Evening"
	else:
		msg="Good Night"
	msg1="Python Language "
	my_dict={"date":date,"msg":msg,"msg1":msg1}
	return render (request,'fifthapp/display.html',context=my_dict)
