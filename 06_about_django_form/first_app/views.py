from django.shortcuts import render, redirect
from django.urls import reverse
from .forms import ReviewForm

# Create your views here.
def rental_review_view(request):
    ## post request --> form contents --> thank you

    if request.method == "POST":
        form = ReviewForm(request.POST)

        if form.is_valid():
            # print(form.cleaned_data)
            form.save()
            return redirect(reverse('first_app:thank_you'))
    
    else:
        form = ReviewForm()

    return render(request, 'first_app/rental_review.html', context={'form' : form})

def thank_you_view(request):
    return render(request, 'first_app/thank_you.html')