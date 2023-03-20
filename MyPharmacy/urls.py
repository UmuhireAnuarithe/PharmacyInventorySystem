
from django.urls import path
from .views import *


urlpatterns = [
    path('pharmacist/',Pharmacist_view.as_view(), name='pharm'),
    
    path('med/',MedicalType_view.as_view(), name='med'),
    path('med/<int:pk>',MedicalType_details.as_view(), name='med_details'),

]