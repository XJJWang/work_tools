from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('query/', views.query, name='query'),
    path('create_project/', views.create_project, name='create_project'),
    path('main/', views.main, name='main'),
    path('login/', views.login, name='login'),
]