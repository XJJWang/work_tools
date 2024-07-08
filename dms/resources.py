from import_export import resources
from .models import Document, Filebook
from import_export import resources, fields
from import_export.widgets import ForeignKeyWidget


class DocumentResource(resources.ModelResource):
    class Meta:
        filebook = fields.Field(
            column_name='filebook',
            attribute='filebook',
            widget=ForeignKeyWidget(Filebook, 'name')  # 假设CSV文件中使用FileBook的name字段作为外键
        )
        model = Document
        fields = ('name', 'filebook', 'put_in_amount', 'amount_now', 'principal',
                  'remark', 'put_in_date', 'short_name')  # 指定要导入导出的字段
        import_id_fields = ('name',)
