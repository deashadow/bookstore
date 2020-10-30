from django.shortcuts import render

from .models import Book

def template(request):
    return render(request, 'template.html');

def bstore(request):
    count = Book.objects.all().count()
    context = {
        'count': count,
    }
    return render(request, 'bstore.html', context);