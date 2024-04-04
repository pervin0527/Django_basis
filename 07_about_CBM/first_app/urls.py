from django.urls import path
from .views import home_view, HomeView, ThankView, ContactFormView, TeacherCreateView, TeacherListView

app_name = 'first_app'
urlpatterns = [
    path('', HomeView.as_view(), name='home'),
    path('thank_you/', ThankView.as_view(), name="thank_you"),
    path('contact/', ContactFormView.as_view(), name='contact'),
    path('create_teacher/', TeacherCreateView.as_view(), name='create_teacher'),
    path('teachers_list/', TeacherListView.as_view(), name='teachers_list')

]
