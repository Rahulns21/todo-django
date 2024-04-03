from django.contrib import admin
from .models import Task

class TaskAdmin(admin.ModelAdmin):
    list_display = ('task', 'is_completed', 'created_at', 'updated_at')
    list_display_links = ('task',)
    list_editable = ('is_completed',)
    search_fields = ('task',)
    list_per_page = 25

admin.site.register(Task, TaskAdmin)