from django.contrib import admin

# Register your models here.
from .models import Student, Company , Recruitment , Contact

admin.site.register (Student)
admin.site.register (Company)
admin.site.register (Recruitment)
admin.site.register (Contact)