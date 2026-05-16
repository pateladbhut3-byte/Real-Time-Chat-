from django.contrib import admin
from .models import About
class AboutAdmin(admin.ModelAdmin):
    list_display=('name','about_info','discription')
admin.site.register(About,AboutAdmin)
# Register your models here.
