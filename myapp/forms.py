from django import forms
from .models import Issue

class IssueForm(forms.ModelForm):
    class Meta:
        model = Issue
        fields = ['userID', 'problem', 'location','time']