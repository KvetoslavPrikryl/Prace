from django.contrib import admin

from .models import Employee, Trained

class EmployeesAdmin(admin.ModelAdmin):
    list_display = ("id", "name", "surname", "card", "merit","info")


class TrainedAdmin(admin.ModelAdmin):
    list_display = ("name", "traineds")

admin.site.register(Employee, EmployeesAdmin)
admin.site.register(Trained, TrainedAdmin)