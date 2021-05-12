from .models import Blog
from django import forms
class ModeForm(forms.ModelForm):
    class Meta:
        model=Blog
        fields=['img','title','desc','author']