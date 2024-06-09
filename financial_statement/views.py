from django.http import HttpResponse
from django.shortcuts import render, redirect

from .models import Project, Section, CapitalFlow


def index(request):
    first_object = Project.objects.first()
    first_object_name = first_object.name
    capital_flow = CapitalFlow.objects.filter(project__name=first_object_name)
    name = first_object.name
    territorial_bond_total = first_object.territorial_bond_total
    treasury_bond_total = first_object.treasury_bond_total
    return render(request, 'financial_statement/index.html', {'name': name, 'territorial_bond_total': territorial_bond_total, 'treasury_bond_total': treasury_bond_total})
    # 导入模型


def query(request):
    first_object = Project.objects.first()
    first_object_name = first_object.name
    treasury_capital_flow = CapitalFlow.objects.filter(project__name=first_object_name).filter(capital_type='Treasury')
    territorial_capital_flow = CapitalFlow.objects.filter(project__name=first_object_name).filter(capital_type='Territorial')

    lst = [t.account for t in treasury_capital_flow]
    print(lst)
    return HttpResponse('chenggong')


def create_project(request):
    if request.method == "POST":
        name = request.POST.get("name")
        territorial_bond_total = request.POST.get("territorial_bond_total")
        treasury_bond_total = request.POST.get("treasury_bond_total")
        new_project = Project()
        new_project.name = name
        new_project.territorial_bond_total = territorial_bond_total
        new_project.treasury_bond_total = treasury_bond_total
        new_project.save()
        return redirect('/financial_statement/')
    if request.method == "GET":
        return render(request, 'financial_statement/create_project.html')


def main(request):
    return render(request, 'financial_statement/main.html')