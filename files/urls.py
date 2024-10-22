from django.urls import path
from . import views

urlpatterns = [
    path('login/', views.custom_login, name='login'),
    path('', views.model_form_upload, name='model_form_upload'),
    path('files/', views.file_list, name='file_list'),
    path('search/', views.search_files, name='search_files'),
    path('delete/<int:pk>/', views.delete_file, name='delete_file'),
]