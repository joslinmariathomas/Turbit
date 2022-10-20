from django.db import models

# Create your models here.
class Turbit(models.Model):
    dt=models.DateField()
    wind = models.FloatField()
    power= models.FloatField()
    
    class Meta:
        ordering = ('dt',)

   
        