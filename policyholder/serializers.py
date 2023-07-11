from rest_framework import serializers
from rest_framework.fields import empty
from .models import QuestionModel, CategoryModel, PolicyModel, PolicyRecordModel, InsurerModel
from core.models import User
from insured.serializers import InsurerSerializer


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        fields = ['id', 'category_name', 'creation_date']
        model = CategoryModel


class PolicySerializer(serializers.ModelSerializer):
    # category = CategorySerializer()
    # policy_name = serializers.HyperlinkedRelatedField(
    #     queryset=PolicyModel.objects.all(), view_name='PolicyDetailView')

    class Meta:
        fields = ['id', 'category', 'policy_name',
                  'permium', 'ternure', 'created_at']
        model = PolicyModel


class PolicyRecordSerializer(serializers.ModelSerializer):
    insurer = serializers.HyperlinkedRelatedField(
        read_only=True,
        view_name='insurer-detail',
        lookup_field='pk')

    policy = serializers.HyperlinkedRelatedField(
        queryset=PolicyModel.objects.all(),
        view_name="policy-detail",
        lookup_field='pk')

    class Meta:
        fields = ['id', 'insurer', 'policy', 'status']
        model = PolicyRecordModel

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        if not self.context['is_staff']:
            self.fields['status'].read_only = True

    def create(self, validated_data):
        insurer_id = self.context['insurer_id']
        insurer = InsurerModel.objects.get(id=insurer_id)
        return PolicyRecordModel.objects.create(insurer=insurer, **validated_data)


class InsurerQuestionsSerializer(serializers.ModelSerializer):
    insurer_id = serializers.IntegerField(read_only=True)
    answer = serializers.CharField(read_only=True)

    class Meta:
        fields = ['id', 'insurer_id', 'answer',
                  'question', 'created_at']
        model = QuestionModel

    def create(self, validated_data):
        insurer_id = self.context['insurer_id']
        return QuestionModel.objects.create(insurer_id=insurer_id, **validated_data)


class AdminQuestionsSerializer(serializers.ModelSerializer):
    email = serializers.EmailField(read_only=True, source='insurer.user.email')
    phone = serializers.CharField(read_only=True, source='insurer.phone')

    class Meta:
        fields = ['id',
                  'question', 'answer', 'email', 'phone',  'created_at']
        model = QuestionModel

    def update(self, instance, validated_data):
        instance.answer = validated_data.get('answer', instance.answer)
        instance.save()
        return instance
