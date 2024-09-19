from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('create_project/', views.create_project, name='create_project'),
    path('main/', views.main, name='main'),
    path('view_my_project/', views.view_my_project, name='view_my_project'),
    path('all_projects/', views.get_all_projects, name="get_all_projects"),
    path('investment_type/',views.add_project_investment_type, name="add_project_investment_type"),
    path('section/', views.add_section, name="add_section"),
    path('captial_flow/', views.add_capital_flow, name="add_capital_flow"),
    path("financial_statement/", views.view_financial_statement, name="view_financial_statement"),
]