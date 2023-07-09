from rest_framework import serializers
from .models import QuestionModel, CategoryModel, PolicyModel, PolicyRecordModel
from insured.serializers import InsurerSerializer


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


# class InsurerPolicySerializer(serializers.ModelSerializer):

#     class Meta:
#         fields = ['id', 'category', 'policy_name',
#                   'permium', 'ternure', 'created_at', 'is_selected']
#         model = PolicyModel
#         read_only_fields = ['category', 'policy_name',
#                             'permium', 'ternure', 'created_at']

#     def update(self, instance, validated_data):
#         instance.is_selected = validated_data.get(
#             PolicyModel, instance.is_selected)
#         instance.save()
#         return instance

    # def create(self, validated_data):
    #     is_selected= self.context['is_selected']
    #     if is_selected:
    #         PolicyModel.objects.create()

    # def update(self, instance, validated_data):


class PolicyRecordSerializer(serializers.ModelSerializer):
    insurer_id = serializers.IntegerField(read_only=True)

    class Meta:
        fields = ['id', 'insurer_id', 'policy', 'status']
        model = PolicyRecordModel

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        if not self.context['is_staff']:
            self.fields['status'].read_only = True

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
    insurer = InsurerSerializer()

    class Meta:
        fields = ['id', 'insurer',
                  'question', 'answer', 'created_at']
        model = QuestionModel

    def update(self, instance, validated_data):
        instance.answer = validated_data.get('answer', instance.answer)
        instance.save()
        return instance
