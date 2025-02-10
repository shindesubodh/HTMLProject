from django.shortcuts import render

# Create your views here.

from django.http import HttpResponse

#Home page/ first page of the web application

def homepage(request):  # This is name of the function. You can call it anything, independent of the url
                        # from where it is being triggered

    num1, num2, num3 = 1,2,3
    # print(num1, num2, num3)
    # if you un-comment above line, then num1, num2, num3 will be printed in the console where you are running the server 
    # i.e. command prompt in our case.

    context = {'num1':1,
               'num2':2,
               'num3':3,
               } # Defining a dictionary which will be passed in render() on next line


   # return HttpResponse ("This is my new home page")
    return render(request, 'HelloApp/index.html',{'context': context})








