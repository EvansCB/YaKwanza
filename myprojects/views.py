from django.shortcuts import render
from myprojects.models import MyProject
# Create your views here.

def myproject_index(request):
    myprojects = MyProject.objects.all()
    context = {
        "myprojects": myprojects
    }
    return render(request, "myprojects/myproject_index.html", context)

def myproject_detail(request, pk):
    myproject = MyProject.objects.get(pk=pk)
    context = {
        "myproject": myproject
    }
    return render(request, "myprojects/myproject_detail.html", context)