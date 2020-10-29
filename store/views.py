from django.shortcuts import render

def template(request):
    return render(request, 'template.html');

def bstore(request):
    return render(request, 'bstore.html');