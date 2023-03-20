from django.contrib import admin
from .models import *

# Register your models here.

@admin.register(Pharmacist)
class PharmacistAdmin(admin.ModelAdmin):
    list_display= ("first_name","last_name","employ_id","Phone_number","gender",)
    list_filter = ("gender","location","joined_date",)
    search_fields =("first_name","last_name","employ_id","Phone_number",)
    ordering = ("employ_id",)
    fieldsets = (
        ('USER',{'fields':("user",)}),
        ('ABOUT PHARMACIST',{'fields':(("first_name","last_name"),"employ_id","Phone_number","gender","location","about",)}),
    )
    
@admin.register(Supplier)
class SupplierAdmin(admin.ModelAdmin):
    list_display= ("first_name","last_name","Phone_number","gender","Work_address","joined_date",)
    list_filter = ("gender","Work_address","joined_date",)
    search_fields =("first_name","last_name","Phone_number",)
    ordering = ("joined_date",)
    fieldsets = (
        ('USER',{'fields':("user",)}),
        ('ABOUT SUPPLIER',{'fields':(("first_name","last_name"),"Phone_number","gender","about",)}),
    )

@admin.register(Medicaltype)
class MedicaltypeAdmin(admin.ModelAdmin):
    list_display= ("Type_name","Created_by","Created_date",)
    list_filter = ("Type_name","Created_by",)
    search_fields =("Type_name","Created_date",)
    ordering = ("Created_date",)
    
    fieldsets = (
        ('USER',{'fields':("user",)}),
        ('MEDICALTYPE DEATALS',{'fields':(("first_name","last_name"),"Work_address","Phone_number","gender","location","about",)}),
    )


@admin.register(Medecine_Category)
class Medecine_CategoryAdmin(admin.ModelAdmin):
    list_display= ("medecine_type","created_by","category_name","created_date",)
    list_filter = ("category_name","created_by",)
    search_fields =("category_name","created_date",)
    ordering = ("category_name",)
    
    fieldsets = (
        ('CATEGORY DEATALS',{'fields':("medecine_type","created_by","category_name",)}),
    )



@admin.register(Medecine_Oder)

class Medecine_OderAdmin(admin.ModelAdmin):
    list_display= ("oder_no","suplier_id","medecine_id","amount","status","ordered_date","created_by",)
    list_filter = ("oder_no","medecine_id","ordered_date",)
    search_fields =("oder_no","created_date",)
    ordering = ("oder_no",)
    
    fieldsets = (
        ('ODER DEATALS',{'fields':("suplier_id","medecine_id","created_by","status","amount",)}),
    )


@admin.register(Medecine_Out)

class Medecine_OutAdmin(admin.ModelAdmin):
    list_display= ("transaction_no","medecine_id","date_out","amount","price","reference_no","done_by",)
    list_filter = ("medecine_id","transaction_no","date_out",)
    price = models.IntegerField()
    search_fields =("transaction_no","done_by","price",)
    ordering = ("date_out",)
    
    fieldsets = (
        ('CATEGORY DEATALS',{'fields':("transaction_no","medecine_id",)}),
    )



@admin.register(Medecine_recieved)
class Medecine_recievedAdmin(admin.ModelAdmin):
    list_display= ("oder_no","medecine_id","suplier_id","amount","created_by","recieved_date",)
    list_filter = ("medecine_id","recieved_date","suplier_id",)
    search_fields =("recieved_date","suplier_id","oder_no",)
    ordering = ("oder_no",)
    
    fieldsets = (
        ('CATEGORY DEATALS',{'fields':("oder_no","created_by","suplier_id","medecine_id","amount",)}),
    )
        

@admin.register(Medecine)
class MedecineAdmin(admin.ModelAdmin):
    list_display= ("batch_no","medecine_name","specification","category_id","remarks","price","retail_price","expiry_date","quantity","created_by","registered_date",)
    list_filter = ("medecine_name","registered_date","category_id",)
    search_fields =("medecine_name","category_id","registered_date",)
    ordering = ("registered_date",)
    

    
    ieldsets = (
        ('CATEGORY DEATALS',{'fields':("batch_no","medecine_name","created_by","specification","category_id","remarks","price","retail_price","expiry_date","quantity",)}),
    )

# @admin.register(Medicaltype)