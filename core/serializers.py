from djoser.serializers import UserCreateSerializer 

class UserCreateSerializers(UserCreateSerializer):
    class Meta(UserCreateSerializer.Meta):
        fields = ["id" , "username"  , "email" , 'password' , 'first_name' , 'last_name']
