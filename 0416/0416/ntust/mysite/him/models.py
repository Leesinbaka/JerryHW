from django.db import models

# Create your models here.
class myself(models.Model):
    name = models.CharField(max_length=20)
    birthday = models.DateField()
    sex = models.CharField(max_length=6,blank=True)
    #姓名、生日、性別
    def __str__(self):
    	return self.name
