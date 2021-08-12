from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='home'),
    path('explore/', views.SchoolListView.as_view(), name='explore'),
    path('explore/school/<int:pk>', views.SchoolDetailView.as_view(), name='school_details'),
    path('explore/upload-csv/', views.upload_csv, name='upload-csv'),
]