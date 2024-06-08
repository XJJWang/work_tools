from django.http import HttpResponse
from django.shortcuts import render

from .models import BasicInfo

def index(request):
    first_object = BasicInfo.objects.first()
    name = first_object.name
    return render(request, 'financial_statement/index.html', {'name': name})
    # 导入模型