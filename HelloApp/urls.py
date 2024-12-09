# this urls.py file was NOT created by default. By default this file is created at project level only
# But we created this at Application level as well - to follow best practice and keep the code clean

from django.urls import path

from . import views # this will allow us to import any functions from views.py file

urlpatterns = [

path ("", views.homepage, name=""),      # the first term under " " is the route name i.e. url path from home page. 
                                # the second term is the view name which will be triggered from the url



]




