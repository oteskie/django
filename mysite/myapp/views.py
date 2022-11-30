from django.shortcuts import render

from django.http import HttpResponse
# Create your views here.

def index(request):
    return HttpResponse("""Building a webpage using Django was a little challenging at first as I didn't know how to do it at first, but with a little of research
    i was successful in firstly installing the framework Django by running the command \"python -m pip install Django\" in my CMD, and it only took few seconds and i was ready to
    start building a webpage. To start a project, i ran the command \"django-admin startproject mysite\" and that created a project called mysite, not to start an app in a project, we
    have to change directories into our project directory and run the command \"python .\manage.py startapp myapp\". To customize the myapp app I created, i had to make a view
    and using the \"HttpResponse\" import, i was able to create a function and return a HttpResponse which is this paragraph i\'m writing, inorder for me to be able to view this view
    on the web, i had to map a url in the urls.py file so i can view this view, in the urls.py file i added this script \"urlpatterns = [path("", views.index, name="index"),]\", finally
    we need to run the server using the command \"python .\manage.py runserver\" and that would make us able to see the view that we created that is mapped under \'app\'.""")
