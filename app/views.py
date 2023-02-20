from django.shortcuts import render
#from django.http import HttpResponse

def PaginaInicial(request):
    return render(request, 'PaginaInicial.html')
def login(request):
    return render(request, 'login.html')
def cadastro(request):
    return render(request, 'cadastro.html')
def Upload(request):
    return render(request, 'Upload.html')
def Download(request):
    return render(request, 'Download.html')