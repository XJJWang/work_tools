from django.contrib import admin # type: ignore
from .models import Project, Section, CapitalFlow, User, Permission, ProjectInfo, ProjectInvestment

admin.site.register(Project)
admin.site.register(Section)
admin.site.register(CapitalFlow)
admin.site.register(User)
admin.site.register(Permission)
admin.site.register(ProjectInfo)
admin.site.register(ProjectInvestment)
