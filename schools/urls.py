from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='home'),
    path('explore/', views.SchoolListView.as_view(), name='explore'),
    path('explore/upload-csv/', views.upload_csv, name='upload-csv'),
]