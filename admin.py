from django.contrib import admin
from .models import Student,Coordinator,CustomUser,TNPOffice,DriveApplication,ActivityApplication

admin.site.register(Student)
admin.site.register(CustomUser)
admin.site.register(Coordinator)
admin.site.register(TNPOffice)
admin.site.register(DriveApplication)
admin.site.register(ActivityApplication)

# Register your models here.
