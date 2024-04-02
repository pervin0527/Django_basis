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
        fields = ["first_name", "last_name", "stars"]