from django.contrib import admin
from cars.models import Car

# Register your models here.

# admin.site.register(Car)

class CarAdmin(admin.ModelAdmin):
    # fields = ['year', 'brand']
    fieldsets = [
        ('TIME Information', {'fields' : ['year']}),
        ('Car Information', {'fields' : ['brand']})
    ]

admin.site.register(Car, CarAdmin)