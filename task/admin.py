from django.contrib import admin
from .models import *
from .models import *

@admin.register(TODO)
class UserAdmin(admin.ModelAdmin):
    list_display = ['id','task_name','date','last_date']