from django import forms


class CsvFileUpload(forms.Form):
    file = forms.FileField()