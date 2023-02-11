from django.db import models

# Create your models here.
class Contact(models.Model):
    name = models.CharField(max_length=122)
    email = models.CharField(max_length=122)
    phone = models.CharField(max_length=12)
    desc = models.TextField()
    date = models.DateField()


    def __str__(self):
      return self.name

class Addrecharge(models.Model):
    phone =models.CharField(max_length=120)
    amount =models.CharField(max_length=120)
    operator =models.CharField(max_length=120)
    desc = models.TextField()
    date =models.DateField()

    def __str__(self):
      return self.phone