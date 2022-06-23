from django.shortcuts import render
from django.http import HttpResponse


def failure_record_views(request):
    return render(request, 'failure.html')
