from rest_framework import serializers
from .models import QuestionModel , CategoryModel , PolicyModel,PolicyRecordModel 

class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        fields = ['id' , 'category_name','creation_date']
        model = CategoryModel


class PolicySerializer(serializers.ModelSerializer):
    # category = CategorySerializer()
    class Meta:
        fields = ['id' , 'category' , 'policy_name' , 'permium', 'ternure' , 'created_at']
        model = PolicyModel


class QuestionsSerializer(serializers.ModelSerializer):
    insurer_id = serializers.IntegerField(read_only =True)
    policy_id = serializers.IntegerField(read_only =True)
    class Meta:
        fileds = ['id' , 'insurer_id' , 'policy_id' , 'question','answer']
        model = QuestionModel


class PolicyRecordSerializer(serializers.ModelSerializer):
    policy = PolicySerializer()
    insurer_id = serializers.IntegerField(read_only = True)
    class Meta:
        fields = ['id' , 'insurer_id' , 'policy' , 'status']
        model = PolicyRecordModel

    def create(self, validated_data):
        insurer_id= self.context['insurer_id']
        return PolicyRecordModel.objects.create(insurer_id=insurer_id , **validated_data)