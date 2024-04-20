from django.contrib.auth.models import User 
from rest_framework import serializers


class UserSerailizer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ["id","username","password"]
        extra_kwargs = {"password" : {"write_only":True}}


    def create (self, validated_date):
        user = User.objects.create_user(**validated_date)
        return user