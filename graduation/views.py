from django.shortcuts import render
from graduation import *
from graduation.serializers import *
from graduation.models import *
from rest_framework.views import APIView
from rest_framework.response import Response
# Create your views here.

class NewAdmissionStudents(APIView):
    def post(self, request):
        serializer = RegistrationSerializer(data=request.data)
        #print('s', serializer)
        if serializer.is_valid(raise_exception=True):
            serializer.save()
        return Response({
                    'status':200,
                    'message':'success',
                    'data':'Registration Successful'
                })
    
    def get(self, request):
        data = NewAdmission.objects.all()
        #print('d',data)
        serializer = RegistrationSerializer(data, many = True)
        #print('s',serializer)
        if serializer.data:
            return Response(serializer.data)
        else:
            return Response({
                    'status':404,
                    'message':'No data',
                    'data':'No data available'
                })
        
    def put(self, request,pk):
        id = NewAdmission.objects.get(id = pk)
        serializer = RegistrationSerializer(id, data=request.data)
        if serializer.is_valid(raise_exception=True):
            serializer.save()
            return Response({
                        'status':200,
                        'message':'success',
                        'data':'Profile updated'
                    })
        else:
            return Response({
                        'status':400,
                        'message':'Something went wrong!',
                        'data':'Failed to update'
                    })
    
    def delete(self, request,pk):
        query = NewAdmission.objects.get(id = pk)
        #print('q',query)
        if query:
            query.delete()
            return Response({
                        'status':200,
                        'message':'success',
                        'data':'Account deleted successfully'
                    })
        return Response({
                        'status':400,
                        'message':'Something went wrong!',
                        'data':'Failed to delete'
                    })
        
        
        

