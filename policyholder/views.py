from django.shortcuts import render, get_object_or_404
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.viewsets import ModelViewSet
from rest_framework.permissions import IsAdminUser, IsAuthenticated, SAFE_METHODS, AllowAny
from .models import PolicyModel, CategoryModel, PolicyRecordModel, QuestionModel
from .serializers import PolicySerializer, CategorySerializer, QuestionsSerializer, PolicyRecordSerializer
# Create your views here.


class CategoryViewset(ModelViewSet):
    permission_classes = [IsAdminUser]
    queryset = CategoryModel.objects.all()
    serializer_class = CategorySerializer


class PolicyViewSet(ModelViewSet):
    queryset = PolicyModel.objects.all()
    serializer_class = PolicySerializer

    def get_permissions(self):
        if self.request.user.is_staff:
            return [AllowAny()]
        elif self.request.method in SAFE_METHODS:
            return [IsAuthenticated()]
        else:
            return [IsAdminUser()]

    def get_serializer_context(self):
        return {'insurer_id': None}


class PolicyRecordViewset(ModelViewSet):
    permission_classes = [IsAdminUser]
    queryset = PolicyRecordModel.objects.all().order_by('status')
    serializer_class = PolicyRecordSerializer


class QuestionViewset(ModelViewSet):
    serializer_class = QuestionsSerializer

    def get_queryset(self):
        if self.request.user.is_staff:
            return QuestionModel.objects.all()
        return QuestionModel.objects.filter(insurer__id=self.request.user.id)

    def get_serializer_context(self):
        if self.request.user.is_staff:
            return {'insurer_id': None, 'policy_id': self.request.user.id}
        return {'insurer_id': self.request.user.id, 'policy_id': None}
