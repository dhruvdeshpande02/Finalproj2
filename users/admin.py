from django.contrib import admin
from .models import Student,Coordinator,CustomUser
from django.contrib.auth.admin import UserAdmin

admin.site.register(Student)
admin.site.register(CustomUser,UserAdmin)
admin.site.register(Coordinator)
# Register your models here.
