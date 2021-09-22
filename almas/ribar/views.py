from django.shortcuts import render
from .models import *



def home(request):
	context = {
	
		
		}
	return render(request, 'index-2.html',context)


def about(request):
	context= {
	
	}
	return render(request, 'about.html', context)

def service(request):
	context= {
	
	}
	return render(request, 'services.html', context)




def gallery(request):
	context= {
	
	}
	return render(request, 'projects.html', context)















def contact(request):
	context= {
	
	}
	return render(request, 'contact.html', context)
# Create your views here.
