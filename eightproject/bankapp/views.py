from django.shortcuts import render

# Create your views here.
def deposit(request):
	msg="CLIENT IS DEPOSIT IN THE ACCOUNT"
	my_dict={'msg':msg}
	return render (request,'bankapp/display.html',context=my_dict)

def withdraw(request):
	msg="CLIENT IS WITHDRAWING FROM THE ACCOUNT"
	my_dict={'msg':msg}
	return render (request,'bankapp/display.html',context=my_dict)


def balance(request):
	msg="CLIENT IS CHEKCING BALANCE IN THE ACCOUNT"
	my_dict={'msg':msg}
	return render (request,'bankapp/display.html',context=my_dict)