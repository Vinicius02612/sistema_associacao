from django.shortcuts import render

# Create your views here.
def pagehome(request):
    return render(request, "global/home/home.html")

#def pagehome(request):
#    return render(request, "homepage/home.html")
