from django.shortcuts import render, get_object_or_404

from .forms import PasteForm
from .models import Paste
from django.http import HttpResponseRedirect, HttpResponse

def paste(request):

	return render(request, 'paste_create.html')

def detail(request,id):
	#Buradaki id bilgisine göre paste detayı gösterilecek
	paste = get_object_or_404(Paste, access_key=id)
	data = {'paste':paste}

	return render(request, 'paste_details.html', data)

def paste_save(request):
	form = PasteForm(request.POST)
	if(form.is_valid()):
		paste = form.save()
		return HttpResponseRedirect('/detail/' + paste.access_key)
	else:
		return HttpResponseRedirect('/paste/')


