from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse

def word_count(request):
	if request.method == 'POST':
		text = request.POST.get('text','')
		word_count = len(text.split())
		return HttpResponse(f"Word count: (word_count)")
	else:
		return HttpResponse("Please submit a form with text input")
