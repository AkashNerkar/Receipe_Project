from django.db import models

# Create your models here.
class UserInformation(models.Model):
    name=models.CharField(max_length=100)
    age=models.IntegerField()
    city=models.CharField(max_length=100)


    def __str__(self):
      return self.name