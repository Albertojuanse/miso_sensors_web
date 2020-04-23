from django.shortcuts import render

def index (request):
    return render(request, 'index.html')

def metaphore (request):
    return render(request, 'metaphore.html')
