
from django.urls import path
from .views import *


urlpatterns = [
    path('pharmacist/',Pharmacist_view.as_view(), name='pharm'),
    path('pharmacist/<int:pk>/',Pharmacist_view.as_view(), name='pharm-details'),
    path('med/',MedicalType_view.as_view(), name='med'),
    path('med/<int:pk>/',MedicalType_view.as_view(), name='med_details'),

]