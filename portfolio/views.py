from django.shortcuts import render
from django.http import HttpResponse
from django.contrib import messages
from . import models
from .models import Contact


def contact(request):
    if request.method == "POST":
        print('post')
        name = request.POST["name"]
        email = request.POST["email"]
        content = request.POST["content"]
        number = request.POST["number"]
        print(name, email, content, number)
        
        if len(name)>1 and len(name)<30:
            pass
        else:
           messages.error(request, 'Length of name should be greater than 2 and less than 30')
           return render(request, 'home.html')
    
        if len(email)>1 and len(email)<30:
          pass
        else:
          messages.error(request, 'invalid email try again')
          return render(request, 'home.html')
    
        if len(number)>2 and len(number)<15:
          pass
        else:
           messages.error(request, 'invalid number try again')
           return render(request, 'home.html') 
    
        ins = models.Contact(name=name, email=email, content=content, number=number)  
        ins.save()
        messages.success(request, 'Thank you for connecting me|| your message have been saved')  
        print('data has been saved to database')
        print('the request is no pass')   
    
    return render(request, 'home.html')