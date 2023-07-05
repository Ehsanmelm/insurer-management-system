from django.shortcuts import render , get_object_or_404
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.viewsets import ModelViewSet
from rest_framework.permissions import IsAdminUser,IsAuthenticated
from .models import PolicyModel , CategoryModel
from .serializers import PolicySerializer,CategorySerializer , QuestionsSerializer
# Create your views here.

class CategoryViewset(ModelViewSet):
    permission_classes = [IsAdminUser]
    queryset = CategoryModel.objects.all()
    serializer_class = CategorySerializer


class PolicyViewSet(ModelViewSet):
    queryset = PolicyModel.objects.all()
    serializer_class = PolicySerializer