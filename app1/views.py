from django.core.mail import send_mail
from django.shortcuts import render,redirect
from django.http import JsonResponse, HttpResponse
from app1.models import *
from app2.models import *
from app1.send_mail import mail
from django.core.files.storage import FileSystemStorage

# Create your views here.

# def index(request):
#     return render(request, 'form2.html')

# def inputs(request):
#     data={}
#     if request.method == 'POST':
#         print(request.POST)
#         name = request.POST.get("name")
#         gender = request.POST.get("gender")
#         issue = request.POST.get("issue")
#         email = request.POST.get("email")
#         image = request.POST.get("image")

#         try:
#             SaveData = savedata(name = name, gender = gender, issue = issue, email = email, image = image).save()
#             data['name'] = name
#             data['gender'] = gender
#             data['issue'] = issue
#             data['email'] = email
#             data['image'] = image
#             data['status'] = 1
#             mail(email,name)
#         except Exception as e:
#             print(e)
#             data['status'] = 0
    
#     return JsonResponse(data, safe = False)

def index(request):
    return render(request, 'newtryform2.html')
    # return render(request, 'indextry.html')


def inputs(request):
    if request.method == 'POST':
        print(request.POST)
        name = request.POST.get("name")
        gender = request.POST.get("gender")
        issue = request.POST.get("issue")
        email = request.POST.get("email")
        image = request.FILES.get("image")
        fss = FileSystemStorage()
        file = fss.save(image.name, image)
        file_url = fss.url(file)

        SaveData = savedata(name = name, gender = gender, issue = issue, email = email, image = image).save()
        mail(email,name)
    
    # return render(request, 'indextry.html')
    
    return render(request, 'newtryform2.html')







