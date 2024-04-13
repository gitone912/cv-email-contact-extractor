from django.urls import path
from . import views

urlpatterns = [
    path('', views.upload_cv, name='upload_cv'),
    path('export/', views.export_to_excel, name='export_to_excel'),
]
