from django.db import models
from phonenumber_field.modelfields import PhoneNumberField
from authentication.models import User

# Create your models here.

class Pharmacist(models.Model):
    
    GENDER_CHOICES =[
        ('SELECT_GENDER', ''),
        ('GENDER_MALE', "Male"),
        ('GENDER_FEMALE', 'Female'),
    ]
    first_name =models.CharField(max_length=255)
    last_name  = models.CharField(max_length=255)
    employ_id = models.CharField(max_length=255)
    Phone_number = PhoneNumberField()
    gender = models.CharField(max_length=255, choices=GENDER_CHOICES)
    location =models.CharField(max_length=15)
    joined_date = models.DateTimeField(auto_now_add=True)
    about = models.CharField(max_length=255)
    user = models.ForeignKey(User, verbose_name="User", on_delete=models.CASCADE)
    
    
    def __str__(self):
        return '{} {}'.format(self.first_name, self.last_name)
    
class Supplier(models.Model):
    
    GENDER_CHOICES =[
        ('SELECT_GENDER', ''),
        ('GENDER_MALE', "Male"),
        ('GENDER_FEMALE', 'Female'),
    ]
    first_name = models.CharField(verbose_name="First Name",max_length=200)
    last_name = models.CharField(verbose_name="Last name", max_length=200)
    Phone_number = PhoneNumberField()
    gender = models.CharField(max_length=20, choices=GENDER_CHOICES,verbose_name="Gender")
    Work_address =models.CharField(max_length=100,verbose_name="Work Address")
    joined_date = models.DateTimeField(auto_now_add=True)
    about = models.CharField(max_length=255,verbose_name="About")
    user = models.ForeignKey(User,verbose_name="User", on_delete=models.CASCADE)

    def __str__(self):
        return '{} {}'.format(self.first_name, self.last_name)
    
    
class Medicaltype(models.Model):
    Type_name = models.CharField(max_length=50)
    
    Created_by = models.ForeignKey(Pharmacist,on_delete=models.CASCADE)
    Created_date = models.DateTimeField(auto_now_add=True)
    
    
    def __str__(self) :
        return self.Type_name

class Medecine_Category(models.Model):
    medecine_type = models.ForeignKey(Medicaltype,on_delete=models.CASCADE)  
    created_by = models.ForeignKey(Pharmacist,on_delete=models.CASCADE)  
    category_name = models.CharField(max_length=255)
    created_date = models.DateTimeField(auto_now_add=True)
    
    
    def __str__(self) :
        return self.category_name
    
class Medecine(models.Model):
    batch_no = models.CharField(max_length=30)
    medecine_name = models.CharField(max_length=255)
    specification = models.TextField(max_length=255)
    category_id = models.ForeignKey(Medecine_Category, on_delete=models.CASCADE)
    remarks = models.TextField()
    price = models.FloatField()
    retail_price = models.FloatField()
    expiry_date = models.DateField( auto_now=False, auto_now_add=False)
    quantity = models.IntegerField()
    created_by = models.ForeignKey(Pharmacist,on_delete=models.CASCADE)
    registered_date =models.DateTimeField(auto_now_add=True)
    
    def __str__ (self):
        return self.medecine_name
    
    
class Medecine_Oder(models.Model):
    
    STATUS_CHOICES =[
        
        ('SELECT_STATUS', ''),
        ('ORDER_STATUS', 'Pending'),
        ('ORDER_STATUS', 'Recieved'),
        
    ]
    
    oder_no = models.CharField(max_length=50)
    suplier_id = models.ForeignKey(Supplier,on_delete=models.CASCADE)
    medecine_id = models.ForeignKey(Medecine,on_delete=models.CASCADE)
    amount = models.IntegerField()
    status = models.CharField(max_length=20,choices=STATUS_CHOICES)
    ordered_date = models.DateTimeField(auto_now_add=True)
    created_by = models.ForeignKey(Pharmacist,on_delete=models.CASCADE)
     
    def __str__(self):
        return '{} {}'.format(self.medecine_id, self.status)
    
class Medecine_recieved(models.Model):
    
    oder_no = models.ForeignKey(Medecine_Oder,max_length=20,on_delete=models.Case)
    suplier_id = models.ForeignKey(Supplier,on_delete=models.CASCADE)
    medecine_id = models.ForeignKey(Medecine,on_delete=models.CASCADE)
    amount = models.IntegerField()
    recieved_date = models.DateTimeField(auto_now_add=True)
    created_by = models.ForeignKey(Pharmacist,on_delete=models.CASCADE)
     
    def __str__(self):
        return '{} {}'.format(self.medecine_id, self.created_by)
    
    
class Medecine_Out(models.Model):
    transaction_no = models.CharField( max_length=50)
    medecine_id = models.ForeignKey(Medecine,on_delete=models.CASCADE)
    price = models.IntegerField()
    date_out = models.DateTimeField(auto_now_add=True)
    done_by = models.ForeignKey(Pharmacist,on_delete=models.CASCADE)
    amount = models.IntegerField()
    reference_no = models.IntegerField()