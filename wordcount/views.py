from django.shortcuts import render
from django.http import HttpResponse

def word_count(request):
	if request.method == 'POST':
		text = request.POST.get('text','')
		word_count = len(text.split())

		return render (request, 'wordcount/result.html', {'word_count': word_count})
	return render(request, 'wordcount/index.html')
