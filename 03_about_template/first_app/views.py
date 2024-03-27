from django.shortcuts import render

# Create your views here.
def example_view(request):
    ## 명시한 first_app 디렉토리는 project 하위의 app 폴더 이름을 참조하는 것이 아님.
    return render(request, "first_app/example.html") ## first_app/templates/first_app/example.html

def variable_view(request):
    my_var = {"first_name" : "Kim", 
              'last_name' : "minjae",
              'some_list' : [1, 2, 3, 4], 
              'some_dict' : {'inside_key' : 'inside_value'},
              'user_logged_in' : False}

    return render(request, 'first_app/variable.html', context=my_var)


def test_view(request):
    return render(request, 'first_app/other.html')