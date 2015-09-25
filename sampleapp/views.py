from django.shortcuts import render_to_response

# Create your views here.
from django.http import HttpResponse

def home(request):
	'''
	Home page view for socket connections 
	'''
	return render_to_response('index.html', )

