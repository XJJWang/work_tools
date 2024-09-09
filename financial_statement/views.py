from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.core.exceptions import ObjectDoesNotExist

from .models import Project, CapitalFlow, User, Permission, ProjectInfo, Section


def index(request):
    return render(request,
                  'financial_statement/base.html')
    # 导入模型


def query(request):
    first_object = Project.objects.first()
    first_object_name = first_object.name
    treasury_capital_flow = CapitalFlow.objects.filter(
        project__name=first_object_name).filter(capital_type='Treasury')

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


def login(request):
    if request.session.get('is_login', None):
        return redirect('/financial_statement/main/')
    if request.method == "POST":
        username = request.POST.get('username')
        password = request.POST.get('password')
        message = "Welcome!"
        if username.strip() and password:
            try:
                user = User.objects.get(username=username)
            except ObjectDoesNotExist:
                message = 'User not exist'
                return render(request, 'financial_statement/login.html', {'message': message})
            if user.password == password:
                request.session['is_login'] = True
                request.session['user_id'] = user.id
                request.session['name'] = user.name
                return redirect('/financial_statement/main/')
            else:
                message = 'Password is uncorrect'
                return render(request, 'financial_statement/login.html', {'message': message})
        else:
            return render(request, 'financial_statement/login.html', {'message': message})

    return render(request, 'financial_statement/login.html')


def view_my_project(request):
    DEFAULT_USER_ID = 1  # fuqiang
    # user_id = request.session.get('user_id', None)
    # if not user_id:
    #     return redirect('/financial_statement/main/')
    user = User.objects.get(pk=DEFAULT_USER_ID)
    projects = Permission.objects.filter(user=user)
    print(locals())
    
    return render(request, 'financial_statement/my_project.html', locals())


def financial(request):
    return render(request, 'financial_statement/financial.html', locals())


def view_information(request):
    DEFAULT_PROJECT_ID = 1
    project = Project.objects.get(pk=DEFAULT_PROJECT_ID)
    infos = ProjectInfo.objects.filter(project=project)
    return render(request, 'financial_statement/project_infomation.html',locals())


def view_finantial_details(request):
    DEFAULT_PROJECT_ID = 1
    project = Project.objects.get(pk=DEFAULT_PROJECT_ID)
    section = Section.objects.filter(project=project)
    section_flow_list = list()
    for s in section:
        capital_flow = CapitalFlow.objects.filter(section=s)
        section_flow_list .append(capital_flow)

    
    calc_flow_by_section(section_flow_list)

    return render(request, 'financial_statement/financial_details.html', locals())



def calc_flow_by_section(section_flow_list):
    for sfl in section_flow_list:
        for s in sfl:
            print(s.account) 


