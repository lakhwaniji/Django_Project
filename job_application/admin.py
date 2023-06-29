from django.contrib import admin
from .models import Form


class FormAdmin(admin.ModelAdmin):
    list_display = ("first","last_name","occupation")
    search_fields = ("first","email")
    list_filter = ("date","occupation")
    ordering = ("first",)
    readonly_fields = ("occupation",)

admin.site.register(Form,FormAdmin)