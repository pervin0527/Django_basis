from django.urls import path
from . import views

app_name = "first_app"

urlpatterns = [
    path("", views.example_view, name="example"),
    path('variable/', views.variable_view, name="variable"),
]