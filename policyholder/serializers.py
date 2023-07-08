from rest_framework import serializers
from .models import QuestionModel, CategoryModel, PolicyModel, PolicyRecordModel


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        fields = ['id', 'category_name', 'creation_date']
        model = CategoryModel


class PolicySerializer(serializers.ModelSerializer):
    # category = CategorySerializer()
    class Meta:
        fields = ['id', 'category', 'policy_name',
                  'permium', 'ternure', 'created_at']
        model = PolicyModel


class PolicyRecordSerializer(serializers.ModelSerializer):
    policy = PolicySerializer()
    insurer_id = serializers.IntegerField(read_only=True)

    class Meta:
        fields = ['id', 'insurer_id', 'policy', 'status']
        model = PolicyRecordModel

    def create(self, validated_data):
        insurer_id = self.context['insurer_id']
        return PolicyRecordModel.objects.create(insurer_id=insurer_id, **validated_data)


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
    class Meta:
        fields = ['id',
                  'question', 'answer', 'created_at']
        model = QuestionModel

    def update(self, instance, validated_data):
        instance.answer = validated_data.get('answer', instance.answer)
        instance.save()
        return instance
