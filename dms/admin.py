from django.contrib import admin
from django.utils.translation import gettext_lazy as _
from django.http import HttpResponse
from django.utils.html import format_html

from import_export.admin import ImportExportModelAdmin

from .models import Bookshelf, Project, Filebook, Document, Cell
from .resources import DocumentResource


admin.site.register(Bookshelf)
admin.site.register(Project)


class FilebookFilter(admin.SimpleListFilter):
    title = _('Filebook')
    parameter_name = 'filebook'

    def lookups(self, request, model_admin):
        filebooks = Filebook.objects.all()
        return [(f.id, f.name) for f in filebooks]

    def queryset(self, request, queryset):
        if self.value():
            return queryset.filter(filebook_id=self.value())
        return queryset


class ProjectFilter(admin.SimpleListFilter):
    title = _('Project')
    parameter_name = 'project'

    def lookups(self, request, model_admin):
        projects = Project.objects.all()
        return [(p.id, p.name) for p in projects]

    def queryset(self, request, queryset):
        if self.value():
            return queryset.filter(filebook__project_id=self.value())
        return queryset


@admin.register(Filebook)
class FilebookAdmin(admin.ModelAdmin):
    autocomplete_fields = ['cell']


@admin.register(Cell)
class CellAdmin(admin.ModelAdmin):
    search_fields = ['bookshelf__name']


@admin.register(Document)
class DocumentAdmin(ImportExportModelAdmin):
    resource_class = DocumentResource
    list_display = ['display_str', 'filebook', 'file_status']
    list_filter = ['filebook__project', 'filebook']
    search_fields = ['short_name']

    def display_str(self, obj):
        return str(obj)  # 返回__str__方法的结果
    display_str.short_description = '名称'  # 设置列的标题

    actions = ['export_selected_documents']

    def export_selected_documents(self, request, queryset):
        resource = self.resource_class()
        dataset = resource.export(queryset)
        response = HttpResponse(dataset.csv, content_type='text/csv')
        response['Content-Disposition'] = 'attachment; filename=selected_documents.csv'
        return response

    def download_link(self, obj):
        if obj.document_file:
            return format_html('<a href="{}" download>下载</a>', obj.document_file.url)
        return "无文件"

    def file_status(self, obj):
        if obj.document_file:
            return format_html('<span style="color: green;">已上传</span>')
        return format_html('<span style="color: red;">未上传</span>')
    file_status.short_description = '文件状态'
    download_link.short_description = '下载文件'

    export_selected_documents.short_description = "导出选中的文件为 CSV"
