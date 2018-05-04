from django.db import models

# Create your models here.
class mymum(models.Model):
    myword = models.CharField(max_length = 300,null=True)

    def __str__(self):
        return self.say