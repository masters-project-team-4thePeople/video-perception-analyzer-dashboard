from django.shortcuts import render


# Create your views here.
def sign_in_page(request):
    return render(request, "pages/sign_in.html")
