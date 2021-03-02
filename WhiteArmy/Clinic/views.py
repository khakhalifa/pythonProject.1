from django.http import HttpResponse
from django.shortcuts import render
from .models import Id

def index (request):
    context = {
        "Patient_info" : Id.objects.all()
    }
    return render(request, "Clinic/index.html")