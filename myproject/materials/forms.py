# materials/forms.py
from django import forms
from .models import Material, File

class MaterialForm(forms.ModelForm):
    class Meta:
        model = Material
        fields = ['title', 'lectures', 'classes', 'labs', 'projects']

class FileForm(forms.ModelForm):
    class Meta:
        model = File
        fields = ['category', 'file']
        widgets = {
            'category': forms.HiddenInput(),
        }
