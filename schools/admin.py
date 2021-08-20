from django.contrib import admin

from schools.models import (
    SchoolsImportFile, 
    SchoolReviews,
    SchoolDetail, 
    School
)

admin.site.register(SchoolsImportFile)
admin.site.register(SchoolReviews)
admin.site.register(SchoolDetail)
admin.site.register(School)
