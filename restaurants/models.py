from django.db import models

# Create your models here.

class Restaurant(models.Model):
	name = models.CharField(max_length = 105)
	description = models.TextField()
	opening_time = models.CharField(max_length = 5) #00:00 
	closing_time = models.CharField(max_length = 5) #00:00

	def __str__(self):
		return self.name