from django.http.response import HttpResponseRedirect
from django.shortcuts import render, redirect
from django.urls import reverse
from django.contrib import messages

from schools.models import School, SchoolDetail, SchoolsImportFile

def index(request):
    template_name = 'schools/index.html'
    context = {}
    return render(request, template_name, context)

def explore_schools(request):
    template_name = 'schools/explore-schools.html'
    context = {}
    return render(request, template_name, context)

def upload_csv(request):
    template_name = 'schools/upload-csv.html'
    context = {}

    if request.method == "GET":
        return render(request, template_name, context)

    try:
        csv_file = request.FILES['csvfile']

        # if not csv_file.name.endswith('.csv'):
        #     messages.error(request, 'THIS IS NOT A CSV FILE')
                
        s = SchoolsImportFile(csv_file)
        s.save()
    except Exception as e:
        messages.error(request,"Unable to upload file. "+repr(e))
    
    return HttpResponseRedirect(reverse("upload-csv"))

