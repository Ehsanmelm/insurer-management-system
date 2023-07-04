from rest_framework import serializers
from .models import QuestionModel , CategoryModel

class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        fields = ['id' , 'category_name','creation_date']
        model = CategoryModel


class PolicySerializer(serializers.ModelSerializer):
    category = CategorySerializer()
    class Meta:
        fields = ['id' , 'category' , 'policy_name' , 'permium', 'ternure' , 'created_at']

class QuestionsSerializer(serializers.ModelSerializer):
    insurer_id = serializers.IntegerField(read_only =True)
    policy_id = serializers.IntegerField(read_only =True)
    class Meta:
        fileds = ['id' , 'insurer_id' , 'policy_id' , 'question','answer']
        model = QuestionModel

