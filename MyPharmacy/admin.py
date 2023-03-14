from django.contrib import admin
from .models import *

# Register your models here.

admin.site.register(Pharmacist)
admin.site.register(Medecine)
admin.site.register(Medecine_Category)
admin.site.register(Medecine_Oder)
admin.site.register(Medecine_Out)
admin.site.register(Medecine_recieved)
admin.site.register(Supplier)
admin.site.register(Medicaltype)