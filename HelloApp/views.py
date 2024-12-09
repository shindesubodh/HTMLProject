from django.shortcuts import render

# Create your views here.

from django.http import HttpResponse

#Home page/ first page of the web application

def homepage(request):  # This is name of the function. You can call it anything, independent of the url
                        # from where it is being triggered

    return HttpResponse ("This is my home page")





