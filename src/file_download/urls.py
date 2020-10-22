from django.urls import path
from .import views

urlpatterns = [
    
    path('file_download/', views.file_download, name="file_download")
]