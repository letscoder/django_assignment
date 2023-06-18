from django.contrib import admin
from myapp.models import Issue
class myappadmin(admin.ModelAdmin):
    list_display=('issueID','userID')
    
admin.site.register(Issue,myappadmin)    

# Register your models here.
