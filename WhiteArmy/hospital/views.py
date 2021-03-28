from django.shortcuts import render
from django.http import HttpResponse
from.models import LeadDoctor
# Create your views here.


def index (request):
    context = {
        "Doctor_info" : LeadDoctor.objects.all()
    }
    return render(request, "hospital/index.html")