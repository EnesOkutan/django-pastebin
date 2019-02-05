from django.db import models
from django.utils import timezone
import django
import datetime

import string
import random

class Paste(models.Model):

	class Meta:
		ordering = ["-created_on","access_key"]

	text = models.TextField()
	language = models.CharField(max_length = 25, null = True, blank = True)
	title = models.CharField(max_length = 50, null = True, blank = True)
	name = models.CharField(max_length = 50)
	created_on = models.DateField(default = django.utils.timezone.now) #Cron dosyasındaki hata, burada tam yol verilerek düzeltilmiştir.(django.utils.timezone.now)
	time_out = models.DateField(null = True, blank = True)
	access_key = models.CharField(max_length = 10)

	NEVER = "never"
	ONE_DAY = "1d"
	ONE_WEEK = "1w"
	ONE_MONTH = "1m"
	ONE_YEAR = "1y"

	def get_new_expiration_datetime(self, expiration):

		expiration_datetime = timezone.now()

		if expiration == self.ONE_DAY:
			expiration_datetime += timezone.timedelta(days=1)
		elif expiration == self.ONE_WEEK:
			expiration_datetime += timezone.timedelta(weeks=1)
		elif expiration == self.ONE_MONTH:
			expiration_datetime += timezone.timedelta(days=30)
		elif expiration == self.ONE_YEAR:
			expiration_datetime += timezone.timedelta(days=365)
		else:
			expiration_datetime = None

		return expiration_datetime


	def set_text_syntax(self, language):
		from pygments import highlight
		from pygments.lexers import get_lexer_by_name
		from pygments.formatters import HtmlFormatter

		lexer = get_lexer_by_name(language, stripall=True)
		formatter = HtmlFormatter(linenos=True, cssclass="highlight")
		text = highlight(self.text, lexer, formatter)
		
		self.text = text
		
		return text

	def set_access_key(self):
		key = self.generate_access_key()
		while Paste.objects.filter(access_key=key):
			key = generate_access_key()

		self.access_key = key

	@staticmethod
	def generate_access_key(size = 10, chars = string.ascii_uppercase + string.digits + string.ascii_lowercase):
		return ''.join(random.choices(chars, k = size))