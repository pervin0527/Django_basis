from django.urls import path
from . import views

app_name = 'first_app'

urlpatterns = [
    path('rental_review/', views.rental_review_view, name='rental_review'),
    path('thank_you/', views.thank_you_view, name='thank_you')
]
