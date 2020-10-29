from django.db import models

# Create your models here.
class Trainer_info(models.Model):
	FIRST_NAME = models.CharField(max_length=50)
	LAST_NAME = models.CharField(max_length=50)
	DOMAIN = models.CharField(max_length=50)
	EXPERINCE = models.IntegerField()
	BRANCH = models.CharField(max_length=50)
	GENDER = models.CharField(max_length=50)
	SALARY = models.FloatField()


	class Meta:
		verbose_name = "Tranier_info"
		verbose_name_plural = "Tranier_infos"

		def __str__(self):
			pass
    