from rest_framework import serializers
from .models import *


class Pharmacist_Selrializers(serializers.ModelSerializer):
    class Meta:
        model = Pharmacist
        fields = "__all__"
        
        
class Medical_Type_Selializers(serializers.ModelSerializer):
    class Meta:
        model = Medicaltype
        fields = "__all__"
        