from django.contrib import admin

# Register your models here.
from myprojects.models import MyProject

class MyProjectAdmin(admin.ModelAdmin):
    pass

admin.site.register(MyProject,MyProjectAdmin)
