from django.db import models

# Create your models here.
class myword(models.Model):
	myword = models.CharField(max_length=200)
	def __str__(self):
		return self.say