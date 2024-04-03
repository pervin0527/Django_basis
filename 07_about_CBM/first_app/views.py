from django.shortcuts import render
from django.views.generic import TemplateView, FormView
from .forms import ContactForm

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