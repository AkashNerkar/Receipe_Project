from django.shortcuts import render,redirect

from .models import *
# Create your views here.
from django.http import HttpResponse
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from .models import UserInformation


def home(request):
    return HttpResponse("King Arthur")

def html(request):
    return render(request,"index.html")

def user_input(request):
    if request.method=="POST":
        name=request.POST.get('name')
        age=request.POST.get('age')
        city=request.POST.get('city')
        UserInformation.objects.create(name=name,age=age,city=city)
        return render(request,'user_input.html')

    return JsonResponse({'message': 'Data saved successfully'})
    # # return JsonResponse({'error': 'Invalid request method'})

    # #     return redirect(user_input)
    # return render(request,'user_input.html')
