from django.contrib import admin
from .models import CV

# Register your models here.
class CVadmin(admin.ModelAdmin):




    def has_add_permission(self, request):
        return True

    def delete(self, request, obj=None):
        return True



admin.site.register(CV,CVadmin)