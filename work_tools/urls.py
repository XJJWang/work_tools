from django.contrib import admin
from django.urls import include, path

urlpatterns = [
    path('financial_statement/', include('financial_statement.urls')),
    path('admin/', admin.site.urls),
]