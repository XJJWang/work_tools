from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('create_project/', views.create_project, name='create_project'),
    path('main/', views.main, name='main'),
    path('view_my_project/', views.view_my_project, name='view_my_project'),
    path('all_projects/', views.get_all_projects, name="get_all_projects"),
]