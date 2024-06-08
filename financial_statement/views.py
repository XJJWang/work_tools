from django.http import HttpResponse
from django.shortcuts import render

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
    lst = list()
    for a in treasury_capital_flow:
        account = a.account
        lst.append(account)
    print(lst)
    total = sum(lst)
    print(total)
    return HttpResponse('chenggong')


# def territorial_bond_details(account):
    