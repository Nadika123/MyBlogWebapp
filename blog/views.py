from django.shortcuts import render
from django.http import HttpResponse

def home(requests):
	return render(requests,'blog/home.html')
def about(requests):
	return render(requests,'blog/about.html')

	
# Create your views here.
