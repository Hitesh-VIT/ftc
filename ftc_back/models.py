from django.db import models
from django.contrib.auth.models import User
class Question(models.Model):
	questionid=models.IntegerField()
	question=models.CharField(max_length=100)
	answer=models.CharField(max_length=100)
	strictness=models.CharField(max_length=50)
	level=models.IntegerField(default=0)
class Teams(models.Model):
	user=models.OneToOneField(User)
	level=models.IntegerField(default=0)
	question_attempted=models.IntegerField(default=0)
	question_count=models.IntegerField(default=0)
	name=models.CharField(max_length=50)

	                    
class questions_attempt(models.Model):
	Team=models.ForeignKey(Teams,unique=False,blank=True)
	ques_id=models.ForeignKey(Question,unique=False,blank=True)
class Clues(models.Model):
	clue_id=models.IntegerField()
	clue_lt=models.FloatField()
	clue_ln=models.FloatField()
	clue_question=models.OneToOneField(Question)
	clue_alphabet=models.CharField(max_length=1)
class Tries(models.Model):
	
	Attempts=models.IntegerField(blank=True)
	Teams=models.OneToOneField(Teams)
	
	
	

