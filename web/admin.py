from django.contrib import admin

from .models import Image

# Register your models here.

class UniversalAdmin(admin.ModelAdmin):
    def get_list_display(self, request):
        return [field.name for field in self.model._meta.concrete_fields]


admin.site.register(Image, UniversalAdmin)