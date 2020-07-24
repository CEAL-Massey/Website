from django.db import models
from django.contrib.auth.models import User

class SalesReport(models.Model):
		month = models.IntegerField()
		sales = models.FloatField()
		product = models.CharField(max_length =25)
class chartEntry(models.Model):
		time = models.FloatField()
		reading = models.FloatField()
		metric = models.CharField(max_length = 16)
		type = models.CharField(max_length = 16)
