from django.db import models

# Create your models here.
class post123(models.Model):
	title = models.CharField(max_length=500,blank=True,null=True)
	content = models.CharField(max_length=500,blank=True,null=True)

	def __str__(self):
		return self.title