from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('query/', views.query, name='query'),
    path('create_project/', views.create_project, name='create_project'),
    path('main/', views.main, name='main'),
    path('login/', views.login, name='login'),
    path('view_my_project/', views.view_my_project, name='view_my_project'),
    path('financial/', views.financial, name='financial'),
    path('project_info/', views.view_information, name='view_information'),
    path('financial_details/', views.view_finantial_details, name='financial_details'),
]