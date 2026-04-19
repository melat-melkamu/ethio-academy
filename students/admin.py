from django.contrib import admin
from .models import Student,Teacher
admin.site.register(Student)
admin.site.register(Teacher)
admin.site.site_header = "Ethio Academy Admin"
admin.site.site_title = "Ethio Academy"
admin.site.index_title = "Welcome to Admin Dashboard"




