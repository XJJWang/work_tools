from django.http import HttpResponse
from django.shortcuts import render

from .models import Project

def index(request):
    first_object = Projectr.objects.first()
    name = first_object.name
    territorial_bond_total = first_object.territorial_bond_total
    treasury_bond_total = first_object.treasury_bond_total
    return render(request, 'financial_statement/index.html', {'name': name, 'territorial_bond_total': territorial_bond_total, 'treasury_bond_total': treasury_bond_total})
    # 导入模型