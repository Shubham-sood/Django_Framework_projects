from django.shortcuts import render
from .models import Batsmen_info

# Create your views here.
def display_batsmen(request):
	batsmen=Batsmen_info.objects.all()
	return render (request,'batsmeninfoapp/display.html',{'batsmen':batsmen})
