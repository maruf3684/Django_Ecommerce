from django.db import models

class Catagory(models.Model):
    name=models.CharField(max_length=50,default='none')

    def __str__(self):
        return self.name