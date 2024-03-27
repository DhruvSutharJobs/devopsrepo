from django.contrib import admin
from app.models import Todos

# Register your models here.
class TodosAdmin(admin.ModelAdmin):
    list_display=['title','text']
admin.site.register(Todos,TodosAdmin)