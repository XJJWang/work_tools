from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.core.exceptions import ObjectDoesNotExist
from django.views.decorators.csrf import csrf_exempt

from .models import Project, CapitalFlow, User, Permission, ProjectInfo, Section, ProjectInvestment

def index(request):
    return render(request,
                  'financial_statement/base.html')
    # 导入模型


@csrf_exempt
def add_project_investment_type(request):
    if request.method == "POST":
        project_pk= request.POST.get("pk")
        project = Project.objects.get(pk=project_pk)
        name = request.POST.get("name")
        amount = request.POST.get('amount')

        new_investment_type = ProjectInvestment()
        new_investment_type.name = name
        new_investment_type.project = project
        new_investment_type.amount = amount
        new_investment_type.save()
        return HttpResponse("Save investment type.")


    if request.method == "GET":
        return HttpResponse("GET investment type")


@csrf_exempt
def add_section(request):
    if request.method == "POST":
        project_pk = request.POST.get('pk')
        project = Project.objects.get(pk=project_pk)
        name = request.POST.get('name')
        amount = request.POST.get('amount')

        new_section = Section()
        new_section.name = name
        new_section.project = project
        new_section.amount = amount
        new_section.save()
        return HttpResponse("Save section.")


@csrf_exempt
def add_capital_flow(request):
    if request.method == "POST":
        project_pk = request.POST.get('project_pk')
        section_pk = request.POST.get('section_pk')
        project = Project.objects.get(pk=project_pk)
        section = Section.objects.get(pk=section_pk)

        pay_time = request.POST.get('pay_time')
        amount = request.POST.get('amount')
        capital_type = request.POST.get('capital_type')
        remark = request.POST.get('remark')

        CapitalFlow.objects.create(
    project=project,
    section=section,
    pay_time=pay_time,
    amount=amount,
    capital_type=capital_type,
    remark=remark,
)
    return HttpResponse('Save capital flow.')

def sections_payment(capital_flow):
    capital_flow_dict = {}
    for cf in capital_flow:
        section = cf.section
        amount = cf.amount

        if section in capital_flow_dict:
            capital_flow_dict[section].append(amount)
        else:
            capital_flow_dict[section] = [amount]
    return capital_flow_dict


def investment_type_payment(capital_flow):
    capital_flow_dict = {}
    for cf in capital_flow:
        capital_type = cf.capital_type
        amount = cf.amount



    

def total_payment():
    pass 


def view_financial_statement(request):
    if request.method == "GET":
        pk = request.GET.get('pk')
        all_capital_flow = CapitalFlow.objects.filter(project__pk=pk)
        capital_flow_dict = sections_payment(all_capital_flow)
        print(capital_flow_dict)
        return HttpResponse('View financial statement')


def get_all_projects(request):
    projects = Project.objects.all()
    for p in projects:
        print(p.id)
    return HttpResponse(projects)


@csrf_exempt
def create_project(request):
    if request.method == "POST":
        name = request.POST.get("name")
        print(name)
        abbr = request.POST.get("abbr")
        year = request.POST.get("year")
        new_project = Project()
        new_project.name = name
        new_project.abbr = abbr
        new_project.year = year
        new_project.save()
        return HttpResponse("Save project")
    if request.method == "GET":
        return HttpResponse('GET create project')


def main(request):
    return render(request, 'financial_statement/main.html')


def view_my_project(request):
    DEFAULT_USER_ID = 1  # fuqiang
    # user_id = request.session.get('user_id', None)
    # if not user_id:
    #     return redirect('/financial_statement/main/')
    user = User.objects.get(pk=DEFAULT_USER_ID)
    projects = Permission.objects.filter(user=user)
    print(locals())
    
    return render(request, 'financial_statement/my_project.html', locals())


def view_information(request):
    DEFAULT_PROJECT_ID = 1
    project = Project.objects.get(pk=DEFAULT_PROJECT_ID)
    infos = ProjectInfo.objects.filter(project=project)
    return render(request, 'financial_statement/project_infomation.html',locals())



