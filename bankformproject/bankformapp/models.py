from django.db import models

# Create your models here.
class AccDetails(models.Model):
	FIRST_NAME = models.CharField(max_length=50)
	LAST_NAME = models.CharField(max_length=50)
	DOB = models.DateField()
	ADDRESS = models.CharField(max_length=50)
	ACCTYPE = models.CharField(max_length=50)
	PAN_NO = models.CharField(max_length=50)
	class Meta:
		verbose_name = "AccDetails"
		verbose_name_plural = "AccDetailss"
		def __str__(self):
			pass
    