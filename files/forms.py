from django import forms
from .models import Document

class DocumentForm(forms.ModelForm):
    class Meta:
        model = Document
        fields = ('description', 'document',)
        labels = {
            'description': '文件描述',
            'document': '文件',
        }