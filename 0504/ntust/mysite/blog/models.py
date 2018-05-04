from django.db import models
from django.utils import timezone
# Create your models here.
class Post(models.Model):
    text = models.TextField(null=True)
    created_date = models.DateTimeField(default=timezone.now)
    published_date = models.DateTimeField(blank=True,null=True)

    def publish(self):
        self.published_date = timezone.now()
        self.save()
        
    def __str__(self):
        return self.post