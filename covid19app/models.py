from django.db import models



class Covid19C(models.Model):
    id = models.AutoField(primary_key=True)
    CountryName = models.CharField(max_length=50)
    Date = models.CharField(max_length=50)


    def __str__(self):
        return self.CountryName