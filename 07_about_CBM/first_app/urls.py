from django.urls import path
from .views import home_view, HomeView, ThankView, ContactFormView, TeacherCreateView, TeacherListView, TeacherDetailView, TeacherUpdateView, TeacherDeletView

app_name = 'first_app'
urlpatterns = [
    path('', HomeView.as_view(), name='home'),
    path('thank_you/', ThankView.as_view(), name="thank_you"),
    path('contact/', ContactFormView.as_view(), name='contact'),
    path('create_teacher/', TeacherCreateView.as_view(), name='create_teacher'),
    path('teachers_list/', TeacherListView.as_view(), name='teachers_list'),

    ## domain.com/first_app/teacher_detail/1
    ## domain.com/first_app/teacher_detail/2 와 같은 패턴을 갖도록 만들자.
    path('teacher_detail/<int:pk>/', TeacherDetailView.as_view(), name='detail_teacher'),

    path('update_teacher/<int:pk>/', TeacherUpdateView.as_view(), name='update_teacher'),

    path('delete_teacher/<int:pk>/', TeacherDeletView.as_view()),
]
