from django.shortcuts import render,redirect

from django.http import HttpResponse
from .models import *


def vege(request):
    if request.method == "POST":
        data = request.POST
        receipe_image = request.FILES.get('receipe_image')
        receipe_name = data.get('receipe_name')
        receipe_desc = data.get('receipe_desc')

        # Create a new Receipe object
        Receipe.objects.create(
            receipe_name=receipe_name,
            receipe_desc=receipe_desc,
            receipe_image=receipe_image,
        )
        return redirect('/vege/')
        # Query all receipes
    queryset = Receipe.objects.all()
        # Redirect to a different page or the same page after successful creation
        

    

    # Filter receipes based on search query if provided
    if request.GET.get("search"):
        queryset = queryset.filter(receipe_name__icontains=request.GET.get("search"))

    context = {'receipes': queryset}
    
    return render(request, "vege.html", context)
    


def delete(request,id):
    queryset=Receipe.objects.get(id=id)
    queryset.delete()
    return redirect("vege")


def Update_receipe(request,id):
     
    queryset=Receipe.objects.get(id=id)

    if request.method=="POST":
        data =request.POST

        receipe_image=request.FILES.get('receipe_image')
        receipe_name = data.get('receipe_name')
        receipe_desc = data.get('receipe_desc')

        queryset.receipe_name=receipe_name
        queryset.receipe_desc=receipe_desc

        if receipe_image:
            queryset.receipe_image=receipe_image

            queryset.save()
        return redirect('/vege/')
    context= {'receipes': queryset}

    
    return render(request,"Updated_vege.html",context)


