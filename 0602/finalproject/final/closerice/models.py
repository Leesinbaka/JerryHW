from django.db import models

# Create your models here.
class City(models.Model):
    taipei = 'TP'
    taichung = 'TC'
    taoyuan = 'TY'
    yilan = 'YL'
    Citychoice = (
        (taipei, 'taipei'),
        (taichung, 'taichung'),
        (taoyuan, 'taoyuan'),
        (yilan, 'yilan'),
    )
    Cityname = models.CharField(
        max_length=2,
        choices=Citychoice,
    )

    def City(self):
        return self.Cityname in (self.taipei)
class district(models.Model):
    gongguan = 'GG'
    districtchoice = (
        (gongguan,'gongguan'),
    )
    districtname = models.CharField(max_length=10,choices=districtchoice)
class Restaurants(models.Model):
    name = models.CharField(max_length=100)
    content = models.TextField(blank= True)
    wifi = models.BooleanField()
    address = models.CharField(max_length=100)
    price = models.CharField(max_length=100,blank=True)
    worktime = models.CharField(max_length=100,blank=True)
    def __str__(self):
        return self.name
class Post(models.Model):
    title = models.CharField(max_length=500)
    contentforpost = models.CharField(max_length=500)
    publish_time = models.DateTimeField(auto_now_add=True)
    def __str__(self):
        return self.title
