from django.shortcuts import render
from django.http import HttpResponse


def links(request):
    return render(request, 'config/links.html', context={'name': 'links'})
