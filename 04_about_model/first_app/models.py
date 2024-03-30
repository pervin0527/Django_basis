from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator

# Create your models here.
class FirstClass(models.Model): ## Define Table
    ## Define Attributes
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    age = models.IntegerField(validators=[MinValueValidator(0), MaxValueValidator(100)])
    height = models.IntegerField(default=160, validators=[MinValueValidator(120), MaxValueValidator(300)]) ## default=0, null=True

    def __str__(self):
        return f"First Name : {self.first_name}, Last Name : {self.last_name}, \
                 Age : {self.age}, Height : {self.height}"