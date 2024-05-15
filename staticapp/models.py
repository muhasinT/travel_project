from django.db import models

# Create your models here.
class place(models.Model):
    name=models.CharField(max_length=250)
    img=models.ImageField(upload_to='pics')
    desc=models.TextField()

    def __str__(self):
        return self.name

class Team(models.Model):
    member=models.CharField(max_length=250)
    imag=models.ImageField(upload_to='pics')
    dept=models.TextField()

    def __str__(self):
        return self.member