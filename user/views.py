from django.shortcuts import render, redirect
from urllib import request
from django.contrib.auth.decorators import login_required
from rest_framework.views import APIView
from .serializers import UploadSerializer
from .models import AdminUpload
from rest_framework.response import Response
from gateway.authentication import Authentication
from rest_framework.permissions import IsAuthenticated
import json
# Create your views here.



class UploadView(APIView):
    authentication_classes = [Authentication]
    permission_classes = [IsAuthenticated]
    def post(self, request):
        if request.method == 'POST':
            serializer = UploadSerializer(data=request.data)
            if serializer.is_valid(raise_exception=True):
                serializer.save()
            return Response ({
                'success': True
            })
                


    def get(self, request):
        data = AdminUpload.objects.all()
        serializer = UploadSerializer(data, many= True)
        return Response(serializer.data)









