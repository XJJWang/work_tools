from django.contrib import admin

from .models import Bookshelf, Project, Filebook, Document

admin.site.register(Bookshelf)
admin.site.register(Project)
admin.site.register(Filebook)
admin.site.register(Document)