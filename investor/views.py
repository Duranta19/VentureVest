from django.shortcuts import render
from django.http import HttpResponse
from auths.models import Auts
# Create your views here.
def home(request,investor_id):
    profile = Auts.objects.filter(id = investor_id).values()
    print(profile)

    return HttpResponse(investor_id)