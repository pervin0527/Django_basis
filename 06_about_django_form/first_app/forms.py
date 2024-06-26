from django import forms
from django.forms import ModelForm
from .models import ReviewModel

# class ReviewForm(forms.Form):
#     first_name = forms.CharField(label='Frist Name', max_length=100)
#     last_name = forms.CharField(label='Last Name', max_length=100)
#     email = forms.EmailField(label='Email')
#     review = forms.CharField(label='Please write your review here', 
#                              widget=forms.Textarea(attrs={'class' : 'myform',
#                                                           'rows' : '2',
#                                                           'cols' : '2'}))
    
class ReviewForm(ModelForm):
    ## ReviewModel에 대한 Form을 생성.
    class Meta:
        model = ReviewModel
        # fields = ["first_name", "last_name", "stars"]
        fields = "__all__" ## 자동으로 모든 모델 필드를 폼 필드로 전달(또는 맵핑) 하라는 것.

        labels = {
            'first_name' : "Your First Name",
            'last_name' : "Last Name",
            'stars' : "Rating"
        }

        error_messages = {
            'stars' : {
                'min_value' : "MIN VALUE is 1",
                'max_value' : "MAX VALUE is 5"
            }
        }