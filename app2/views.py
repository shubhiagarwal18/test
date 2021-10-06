from django.shortcuts import render

from app1.models import savedata
from django.http import JsonResponse, HttpResponse
from app1.models import *
from app2.models import *

# Create your views here.

def show_data(request):
    return render(request, 'table.html')


def view(request):
    d={}
    viewdata = savedata.objects.filter().values()
    d['user_data']=list(viewdata)
    return JsonResponse(d, safe=False)


# def search(request):
#     return

def delete(request):
    d={}
    id=request.GET.get("id")
    try:
        savedata.objects.filter(id=id).delete()
        d['status'] = 1
    except:
        d['status'] = 0
    return JsonResponse(d, safe=False)