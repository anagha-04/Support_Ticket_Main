from rest_framework import serializers

from userapp.models import User

class UserRegisterSerializer(serializers.ModelSerializer):

    class Meta:

        model = User

        fields =['username','password','email']