from rest_framework import serializers
from ftc_back.models import Question,Teams,Clues


class AnswerSerializer(serializers.ModelSerializer):
	
	class Meta:
		model=Question
		fields= ('id_ques','ans')
class TeamSerializer(serializers.ModelSerializer):
	
	class Meta:
		model=Teams
		fields=('user','level','question_attempted','question_count')
class QuestionSerializer(serializers.ModelSerializer):
	
	class Meta:
		model=Question
		fields= ('ques','strictness','id_ques')
class ClueSerializer(serializers.ModelSerializer):
	class Meta:
		model=Clues
		fields=('clue_id','clue_lt','clue_ln')

	
		
	
