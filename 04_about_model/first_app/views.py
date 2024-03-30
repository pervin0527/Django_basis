from django.shortcuts import render
from . import models

# Create your views here.
def user_list_view(request):
    all_users = models.FirstClass.objects.all()

    return render(request, 'first_app/all_users.html', context={'whole_users' : all_users})