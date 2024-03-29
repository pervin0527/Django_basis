from django.db import models

# Create your models here.
class FirstClass(models.Model): ## Define Table
    ## Define Attributes
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    age = models.IntegerField()

    def __str__(self):
        return f"First Name : {self.first_name}, Last Name : {self.last_name}, Age : {self.age}"