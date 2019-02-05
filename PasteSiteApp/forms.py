from django import forms
from .models import Paste

from django.utils import timezone

class PasteForm(forms.Form):

	text = forms.CharField(max_length = 1000)
	language = forms.CharField(max_length = 20)
	title = forms.CharField(max_length = 50, required = False)
	name = forms.CharField(max_length = 50)
	time_out = forms.CharField(max_length=20)
	
	def save(self):
		paste = Paste(text = self.cleaned_data['text'], language = self.cleaned_data['language'], title = self.cleaned_data['title'], name = self.cleaned_data['name'], time_out = self.cleaned_data['time_out'])
		paste.time_out = paste.get_new_expiration_datetime(paste.time_out)
		paste.set_text_syntax(paste.language)
		paste.set_access_key()
		paste.save()
		return paste