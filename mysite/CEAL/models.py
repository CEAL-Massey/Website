from django.db import models

class SalesReport(models.Model):
		month = models.IntegerField()
		sales = models.FloatField()
		product = models.CharField(max_length =25)
class chartEntry(models.Model):
		time = models.FloatField()
		reading = models.FloatField()
		