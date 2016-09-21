from rest_framework import serializers
from ftc_back.models import Question,Teams,Clues
from django.contrib.auth import authenticate
from django.utils.translation import ugettext_lazy as _
from rest_framework.views import exception_handler





class AnswerSerializer(serializers.ModelSerializer):
	
	class Meta:
		model=Question
		fields= ('questionid','answer')
class TeamSerializer(serializers.ModelSerializer):
	
	class Meta:
		model=Teams
		fields=('level','question_attempted','name')
class Question_getSerializer(serializers.Serializer):
	questionid=serializers.IntegerField()
	
	

class ClueSerializer(serializers.ModelSerializer):
	class Meta:
		model=Clues
		fields=('clue_id','clue_lt','clue_ln')

	
class AuthTokenSerializer(serializers.Serializer):
    username = serializers.CharField(label=_("Username"),required=False)
    password = serializers.CharField(label=_("Password"), style={'input_type': 'password'},required=False)

    def validate(self, attrs):
        username = attrs.get('username')
        password = attrs.get('password')

       
        user = authenticate(username=username, password=password)
        if user is None:
            	attrs['user']='null'
            	return attrs
        attrs['user']=user
        return attrs
class Team_createSerializer(serializers.Serializer):
	name=serializers.CharField()
	
			


	
