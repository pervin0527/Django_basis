from django.shortcuts import render
from django.http.response import HttpResponse

# Create your views here.

## function based view
## app의 urls.py에 연결되어야 함.
def simple_view(request):
    return HttpResponse("Simple View")

def simple_function_view(request):
    return HttpResponse("Simple function view")

## Dynamic Views
"""
def sports_view(request):
    return HttpResponse("Sports Page")

def finance_view(request):
    return HttpResponse("Finance Page")  ## --> 매번 새로운 view를 만들기 번거롭다.
"""

articles = {
    "sports" : "Sports Page",
    "finance" : "Finance Page",
    "politics" : "Politics Page"
}

## topic을 어떻게 입력 받을 것인가??
## 장고에게 topic이 url패턴에서도 동적으로 형성되어야 한다는 것을 인식시켜야한다.
def news_view(request, topic):
    return HttpResponse(articles[topic])

def add_view(request, num1, num2):
    ## domain.com/first_app/num1/num2 --> num1 + num2
    return HttpResponse(str(num1 + num2))