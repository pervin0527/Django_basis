"""
first_app 내부의 뷰에 연결된 URL을 제어하며 프로젝트 레벨의 url에 연결되어야 한다.
"""

from django.urls import path
from . import views

## urlpatterns 리스트는 URL 패턴과 뷰 함수의 매핑을 정의한다.
## Django는 사용자의 요청을 받으면 urlpatterns의 목록을 순차적으로 검색하여 요청된 URL과 일치하는 패턴을 찾는다.
urlpatterns = [
    # path("", views.simple_view), ## domain.com/fisrt_app
    # path("simple_function_view/", views.simple_function_view), ## domain.com/first_app/simple_function_view

    # path("<int:num1>/<int:num2>", views.add_view),
    # path("<str:topic>/", views.news_view),

    path("<int:page_number>/", views.num_page_view),
    path("<str:topic>/", views.news_view, name="topic-page"),

    path("", views.simple_view), ## domain.com/fisrt_app
]