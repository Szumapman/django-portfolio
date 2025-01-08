from django.shortcuts import render
from django.http import HttpResponse


# Create your views here.
def project_list(request):
    # return render(request, "projects/project_list.html")
    return HttpResponse("Hello World!")
