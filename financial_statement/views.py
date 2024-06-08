from django.http import HttpResponse

from .models import BasicInfo

def index(request):
    first_object = BasicInfo.objects.first()
    name = first_object.name
    return HttpResponse("The project name is %s" % name)
    # 导入模型