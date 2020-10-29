from django.db import models

# Create your models here.
class Batsmen_info(models.Model):
	FIRST_NAME = models.CharField(max_length=50)
	LAST_NAME = models.CharField(max_length=50)
	COUNTRY = models.CharField(max_length=50)
	AGE = models.IntegerField()
	RUNS = models.IntegerField()
	AVG = models.FloatField()
	RANK = models.IntegerField()
	PLAYED = models.IntegerField()
	STR = models.IntegerField()
	class Meta:
		verbose_name = "Batsmen_info"
		verbose_name_plural = "Batsmen_infos"
		def __str__(self):
			pass
    