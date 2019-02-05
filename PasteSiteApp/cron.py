from django_cron import CronJobBase, Schedule
from .models import Paste
from django.utils import timezone

from django.db import connection, transaction

class MyCronJob(CronJobBase):
    RUN_EVERY_MINS = 1 # her 1 günde
    ALLOW_PARALLEL_RUNS = True

    schedule = Schedule(run_every_mins=RUN_EVERY_MINS)
    code = 'PasteSiteApp.my_cron_job'    # a unique code

    def do(self):
    	try:
    		Paste.objects.filter(time_out__lte = timezone.now()).delete()
    		vacuum_db() # Veritabanında boşalan alanların fiziksel olarak geri kazanılması için vacuum işlemi yapılıyor.
    		print("İşlem Başarılı")
    	except:
    		print("İşlem Başarısız")
	
def vacuum_db():
	from django.db import connection
	cursor = connection.cursor()
	cursor.execute("VACUUM")
	connection.close()