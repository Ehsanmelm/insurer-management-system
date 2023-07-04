from rest_framework import serializers
from .models import InsurerModel


class InsurerSerializer(serializers.ModelSerializer):
    user_id=  serializers.IntegerField(read_only =True)
    class Meta:
        fields = ['id' ,"user_id", 'phone' , 'address']
        model = InsurerModel

    def create(self, validated_data):
        user_id= self.context["user_id"]
        return InsurerModel.objects.create(user_id=user_id , **validated_data)
    
