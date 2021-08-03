from django.contrib import admin

from schools.models import SchoolsImportFile, School, SchoolDetail

admin.site.register(SchoolDetail)
admin.site.register(School)
admin.site.register(SchoolsImportFile)
