from django.shortcuts import render

# Create your views here.
def pagehome(request):
    return render(request, "home/home.html")
