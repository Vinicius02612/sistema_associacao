from django.shortcuts import render


def addProjeto(request):
    return render(request, 'socios/addProjeto/index.html')