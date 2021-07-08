from django.db import models
from django.contrib.auth.models import User

DIVSION_CHOICE=(
    ("Rajshahi","Rajshahi"),
    ("Dhaka","Dhaka"),
    ("Mymensingh", "Mymensingh"),
    ("Chittagong", "Chittagong"),
    ("Khulna", "Khulna"),
    ("Rangpur", "Rangpur"),
    ("Sylhet", "Sylhet"),
)

class Customer(models.Model):
    user=models.ForeignKey(User,on_delete=models.CASCADE)
    name=models.CharField(max_length=200)
    city=models.CharField(max_length=50)
    locality=models.CharField(max_length=200)
    zipcode=models.IntegerField()
    phone_number = models.CharField(max_length=12,null=True,default=None)
    division=models.CharField(choices=DIVSION_CHOICE,max_length=50)

    def __str__(self):
        return self.name