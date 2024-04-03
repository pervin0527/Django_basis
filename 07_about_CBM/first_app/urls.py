from django.urls import path
from .views import home_view, HomeView, ThankView, ContactFormView

app_name = 'first_app'
urlpatterns = [
    path('', HomeView.as_view(), name='home'),
    path('thank_you/', ThankView.as_view(), name="thank_you"),
    path('contact/', ContactFormView.as_view(), name='contact'),
]
