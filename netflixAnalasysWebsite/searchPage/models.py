from django.db import models

# Create your models here.
class netflixData(models.Model):
    type = models.CharField()
    title = models.CharField()
    director = models.CharField()
    cast = models.CharField()
    country= models.CharField()
    date_added = models.CharField()
    release_year = models.DateField()
    rating = models.CharField()
    duration = models.CharField()
    listed_in = models.CharField()
    description = models.CharField()


