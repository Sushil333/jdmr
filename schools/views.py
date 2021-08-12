from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.shortcuts import render, redirect
from django.contrib import messages
from django.urls import reverse
from django.contrib.admin.views.decorators import staff_member_required

from schools.forms import ImportFileForm
from schools.models import School, SchoolDetail

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


class SchoolDetailView(DetailView):
    model = SchoolDetail
    template_name = 'schools/school_detail.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        return context


# def explore_schools(request):
#     template_name = 'schools/explore-schools.html'
#     schools = School.objects.all()
#     return render(request, template_name, {'schools': schools})

from django.core.paginator import Paginator
@staff_member_required()
def upload_csv(request):
    template_name = 'schools/upload-csv.html'
    form = ImportFileForm()

    if request.method == 'POST':
        form = ImportFileForm(request.POST, request.FILES)

        if form.is_valid():
            form.save()
            return redirect('explore')
    
    school_list = School.objects.all().order_by('school_name')
    paginator = Paginator(school_list, 25)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)

    return render(request, template_name, {'form':form, 'page_obj': page_obj})
    
