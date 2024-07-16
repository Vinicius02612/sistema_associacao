from django.shortcuts import render

# Create your views here.
def page(request):
    context = {'is_page_admin':True}
    return render(request, "admin/home/home.html", context)