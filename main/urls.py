from . import views
from django.urls import path,include

urlpatterns = [
    path('', views.index, name="index"),
    path('exportfile', views.exportFile, name="exportFile"),
    path('exportinfo/<str:code>', views.exportInfo, name="exportInfo"),
    path('importfile', views.importFile, name="importFile"),
    path('file/<str:code>', views.file, name="file"),
  
]

