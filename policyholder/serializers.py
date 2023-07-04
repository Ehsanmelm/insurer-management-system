from rest_framework import serializers
from .models import QuestionModel


class QuestionsSerializer(serializers.ModelSerializer):
    insurer_id = serializers.IntegerField(read_only =True)
    policy_id = serializers.IntegerField(read_only =True)
    class Meta:
        fileds = ['id' , 'insurer_id' , 'policy_id' , 'question','answer']
        model = QuestionModel
        
