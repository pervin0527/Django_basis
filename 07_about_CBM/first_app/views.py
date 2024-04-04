from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import TemplateView, FormView, CreateView, ListView, DetailView, UpdateView, DeleteView
from .forms import ContactForm
from .models import Teacher

# Create your views here.
def home_view(request):
    return render(request, 'first_app/home.html')

class HomeView(TemplateView):
    template_name = 'first_app/home.html'

class ThankView(TemplateView):
    template_name = 'first_app/thank.html'

class ContactFormView(FormView):
    form_class = ContactForm
    template_name = 'first_app/contact.html'

    ## 성공한 경우, 다음으로 이동할 페이지를 명시. html 템플릿이 아니라 url 경로임에 주의.
    success_url = '/first_app/thank_you/'

    ## form의 값을 받고 나면 무엇을 할 것인가??
    def form_valid(self, form):
        print(form.cleaned_data)

        return super().form_valid(form) ## FormView 부모 클래스에 정의된 form_valid 메서드를 호출.
    
class TeacherCreateView(CreateView):
    model = Teacher ## CreateView는 model 클래스 이름을 통해 "template_name"을 결정한다. 즉, first_app/teacher_form.html을 템플릿으로 찾으려 한다.
    fields = "__all__"

    ## 유효성 검사와 저장(.save())를 자동으로 수행한다.
    success_url = reverse_lazy('first_app:teachers_list')

class TeacherListView(ListView):
    ## model_list.html
    model = Teacher
    context_object_name = "teachers_list" ## default : object_list

    ## ListView의 기본작업은 model.objects.all()이지만 queryset을 커스터마이징 할 수도 있다.
    # queryset = Teacher.objects.all() ## default
    queryset = Teacher.objects.order_by('first_name') ## Query를 커스터마이징 하거나, 필터링을 적용할 수 있음.


class TeacherDetailView(DetailView):
    ## model_detail.html
    ## DetailView는 오직 하나의 데이터(레코드)만을 가져온다.
    model = Teacher


class TeacherUpdateView(UpdateView):
    ## 단 하나의 데이터(레코드)에 대해서만 업데이트를 수행.
    model = Teacher

    ## CreateView에서 사용하는 model_form.html을 활용함.(공유함)
    fields = "__all__" ## ['subject']
    success_url = reverse_lazy('first_app:teachers_list')


class TeacherDeletView(DeleteView):
    model = Teacher

    ## model_confirm_delete.html
    success_url = reverse_lazy('first_app:teachers_list')