from django.shortcuts import render

def custom_not_found_view(request, exception):
    return render(request, "error_page.html", status=404)