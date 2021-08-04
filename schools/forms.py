from django import forms

from schools.models import SchoolsImportFile

class ImportFileForm(forms.ModelForm):
    class Meta:
        model = SchoolsImportFile
        fields = ('schools_import',)
