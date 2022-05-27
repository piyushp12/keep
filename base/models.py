from django.db import models

# Create your models here.
class Contact (models.Model):
    name=models.CharField(max_length=122)
    last=models.CharField(max_length=50)
    email=models.CharField(max_length=50)
    phone=models.CharField(max_length=50)

    def __str__(self) -> str:
        return self.name+" "+self.last