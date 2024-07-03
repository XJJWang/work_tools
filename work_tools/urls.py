from django.contrib import admin
from django.urls import include, path

admin.site.site_header = "吗喽之家"  # 更改登录页面和管理页面的标题
admin.site.site_title = "吗喽之家管理后台"  # 更改网站标题
admin.site.index_title = "欢迎来到管理后台"  # 更改首页标题


urlpatterns = [
    path('financial_statement/', include('financial_statement.urls')),
    path('dms/', include('dms.urls')),
    path('admin/', admin.site.urls),
]