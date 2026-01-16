from rest_framework import serializers

from userapp.models import *

class UserRegisterSerializer(serializers.ModelSerializer):

    class Meta:

        model = User

        fields =['username','password','email']

    def create(self, validated_data):

        user = User.objects.create_user(
            username=validated_data['username'],
            password=validated_data['password'],
            email = validated_data['email']
        )
        return user
    
class SupportTicketSerializer(serializers.ModelSerializer):

    class  Meta:

        model = SupportTicketModel

        exclude =('user',)


       