from django.http.response import HttpResponse
from django.shortcuts import render

# Create your views here.


def index(request):
    current_user = request.user
    context={
        'current_user':current_user,
    }
    return render(request,'home.html',context)