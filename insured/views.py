from django.shortcuts import render , get_object_or_404
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.viewsets import ModelViewSet
from rest_framework.permissions import IsAuthenticated
from .models import InsurerModel
from .serializers import InsurerSerializer

# Create your views here.


class InsurerViewSet(ModelViewSet):
    serializer_class = InsurerSerializer
    def get_queryset(self):
        if self.request.user.is_staff:
            queryset = InsurerModel.objects.all()
        
        queryset = InsurerModel.objects.get(user_id=self.request.user.id )

    def get_serializer_context(self):
        return {"user_id" : self.request.user.id} 