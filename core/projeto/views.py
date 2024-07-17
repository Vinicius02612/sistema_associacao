from django.shortcuts import render

# Create your views here.
def home_page(request):
    return render(request, 'admin/projeto/addProjeto.html')

def upadate_projeto(request):
    return render(request, 'admin/projeto/atualizar_projeto.html')


def search_projeto(request):
    return render(request,'admin/projeto/buscar_projeto.html')