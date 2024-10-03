from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import *
from .serializers import *

# Create your views here.

class StudentView(APIView):
    
    def get(self, request, *args, **kwargs):
        result = Students.objects.all()
        serializers = Studentserializer(result, many=True)
        return Response({'status': 'success', "students":serializers.data}, status=status.HTTP_200_OK)
    
    def post(self, request):
        serializer = Studentserializer(data=request.data, many=True)
        if serializer.is_valid():
            serializer.save()
            return Response({"status": "success", "data": serializer.data}, status=status.HTTP_201_CREATED)
        else:
            return Response({"status": "error", "data": serializer.errors}, status=status.HTTP_400_BAD_REQUEST)
        
def index(request):
    return render(request, 'index.html')