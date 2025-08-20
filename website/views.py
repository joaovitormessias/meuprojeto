from django.shortcuts import render

def home(request):
    return render(request, 'website/home.html')

def sobre(request):
    return render(request, 'website/sobre.html')

def contato(request):
    return render(request, 'website/contato.html')
