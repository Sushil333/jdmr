from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='home'),
    path('explore/', views.explore_schools, name='explore'),
    path('explore/upload-csv/', views.upload_csv, name='upload-csv'),
]