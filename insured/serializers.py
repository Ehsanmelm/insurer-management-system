from rest_framework import serializers
from .models import InsurerModel


class InsurerSerializer(serializers.ModelSerializer):
    user_id=  serializers.IntegerField(read_only =True)
    class Meta:
        fields = ['id' ,"user_id", 'phone' , 'address']
        model = InsurerModel
