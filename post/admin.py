from django.contrib import admin

# Register your models here.
from .models import Post

class PostAdmin(admin.ModelAdmin):
    list_filter = ['Publish','created']
    list_display = ['title','created','Publish']
    search_fields = ['tile','content']



    def has_add_permission(self, request):
        return True

    def delete(self, request, obj=None):
        return True



admin.site.register(Post,PostAdmin)
