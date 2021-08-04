from django.views.generic.list import ListView
from django.shortcuts import render, redirect
from django.contrib import messages
from django.urls import reverse

from schools.forms import ImportFileForm
from schools.models import School

def index(request):
    template_name = 'schools/index.html'
    context = {}
    return render(request, template_name, context)


class SchoolListView(ListView):
    model = School
    paginate_by = 5 # if pagination is desired

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        return context


# def explore_schools(request):
#     template_name = 'schools/explore-schools.html'
#     schools = School.objects.all()
#     return render(request, template_name, {'schools': schools})

def upload_csv(request):
    template_name = 'schools/upload-csv.html'
    form = ImportFileForm()

    if request.method == 'POST':
        form = ImportFileForm(request.POST, request.FILES)

        if form.is_valid():
            form.save()
            return redirect('explore')
    return render(request, template_name, {'form':form})
    
