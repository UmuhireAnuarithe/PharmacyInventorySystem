
from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework import status, permissions
from .models import *
from rest_framework.response import Response
from .serializers import *
### for viewsets
from authentication.models import User
from django.shortcuts import get_object_or_404
# from MyPharmacy.serializers import UserSerializer
from rest_framework import viewsets
from rest_framework.response import Response

# Create your views here.



class Pharmacist_view(APIView):
    # add permission to check if user is authenticated
    # permission_classes = [permissions.IsAuthenticated]

    # 1. List all
    def get(self, request):
        '''
        List all the Medecine  types for given requested user
        '''
        all_pharmacist = Pharmacist.objects.all()
        serializer = Pharmacist_Selrializers(all_pharmacist, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
    
    
    def post(self, request, *args, **kwargs):
        '''
        Create the Pharmacist
        '''
        serializer = Pharmacist_Selrializers(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


    def delete(self, request, id=None):
        pharmacist = Pharmacist.objects.filter(id=id)
        pharmacist.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
  
  
   
class MedicalType_view(APIView):
    # add permission to check if user is authenticated
    # permission_classes = [permissions.IsAuthenticated]

    # 1. List all
    def get(self, request):
        '''
        List all the Medecine  types for given requested user
        '''
        medecine_types = Medicaltype.objects.all()
        serializer = Medical_Type_Selializers(medecine_types, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
    
    
    def post(self, request, *args, **kwargs):
        '''
        Create the medecine Types with given data
        '''
        # data = {
        #     'Type_name': request.data.get('Type_name'), 
        #     'Created_by': request.user.id,
        #     'Created_date': request.data.get('Created_date'), 
        # }
        serializer = Medical_Type_Selializers(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    
    def put(self, request, pk=None):
        # medecine_type = self.get_object(pk)
        medecine_type = Medicaltype.objects.get(id=pk)
        serializer = Medical_Type_Selializers(medecine_type, data=request.data)
        
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)
    

    
    
    
    def delete(self, request, pk=None):
        # medecine_type = self.get_object(pk)
        medecine_type = Medicaltype.objects.get(id=pk)
        medecine_type.delete()
        return Response({"status":"deleted"})
    
    
    
    
    
# class MedicaltypeViewSet(viewsets.ViewSet):
#     """
#     A simple ViewSet for listing or retrieving medecine types.
#     """
#     def list(self, request):
#         medical_type = User.objects.all()
#         serializer = Medical_Type_Selializers(medical_type, many=True)
#         return Response(serializer.data)

#     def retrieve(self, request, pk=None):
#         medical_type = User.objects.all()
#         medtype= get_object_or_404(medical_type, pk=pk)
#         serializer = Medical_Type_Selializers(medtype)
#         return Response(serializer.data)
    