from django.shortcuts import render

def index(request): 
    return HttpResponse(""" Welcome the Library.\n
        You will have access to all the books and features.""")

