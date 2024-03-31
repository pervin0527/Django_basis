from django.shortcuts import render, redirect
from django.urls import reverse
from . import models

# Create your views here.
def list_view(request):
    all_cars = models.Car.objects.all()

    context = {'all_cars' : all_cars}
    return render(request, 'cars/list.html', context=context)

def add_view(request):
    # print(request.POST)
    if request.POST:
        brand = request.POST["brand"]
        year = int(request.POST["year"])

        models.Car.objects.create(brand=brand, year=year)

        return redirect(reverse('cars:list'))
    else:
        return render(request, 'cars/add.html')

def delete_view(request):
    if request.POST:
        pk = request.POST["primary_key"]
        try:
            models.Car.objects.get(pk=pk).delete()
            return redirect(reverse('cars:list'))
        except:
            print("Primary Key Not Found.")
            return redirect(reverse('cars:list'))
    else:
        return render(request, 'cars/delete.html')