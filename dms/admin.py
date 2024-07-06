from django.contrib import admin
from django.contrib.admin.widgets import AutocompleteSelect
from django.db import models


from .models import Bookshelf, Project, Filebook, Document, Cell

admin.site.register(Bookshelf)
admin.site.register(Project)

admin.site.register(Document)

@admin.register(Filebook)
class FilebookAdmin(admin.ModelAdmin):
    autocomplete_fields = ['cell']

@admin.register(Cell)
class CellAdmin(admin.ModelAdmin):
    search_fields = ['bookshelf__name']


# @admin.register(Filebook)
# class FilebookAdmin(admin.ModelAdmin):
#     # 其他 admin 配置...

#     def get_form(self, request, obj=None, **kwargs):
#         form = super().get_form(request, obj, **kwargs)
#         form.base_fields['cell'].widget = AutocompleteSelect(
#             Filebook._meta.get_field('cell').remote_field,
#             admin.site,
#         )
#         return form

# @admin.register(Cell)
# class CellAdmin(admin.ModelAdmin):
#     search_fields = ['name']  # 根据需要选择搜索字段