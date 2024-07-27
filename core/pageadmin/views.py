from django.shortcuts import render

# Create your views here.
def page(request):
    is_page_admin = True
    return render(request, "admin/home/home.html", {'page_admin': is_page_admin})