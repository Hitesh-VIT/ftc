from django.shortcuts import render,redirect
from django.http import HttpResponse
from rest_framework import generics
from ftc_back.models import Question,Teams,questions_attempt
from ftc_back.serializers import QuestionSerializer,AnswerSerializer,TeamSerializer
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated
import random




@api_view(['GET'])
@permission_classes((IsAuthenticated, ))
def Question_v(request):
	user=request.user
	team=Teams.objects.get(user=user)
	team.level_checker()
	team.save()
	
	question_attempt_list=[]
	question_list_all=[]
	try :
		q1=questions_attempt.objects.filter(Team=team)
		for i in q1:
			question_attempt_list.append(i.ques_id.id_ques)
	except TypeError:
		pass
	
	
	question=Question.objects.filter(level=team.level)
	for j in question:
		question_list_all.append(j.id_ques)
	final_list=set(question_list_all)-set(question_attempt_list)
	final_list=list(final_list)
	index=len(final_list)-1
	if index >=0 :
		index=random.randint(0,index)
	else:
		index=index+1
	question_id=final_list[index]
	
	
	question1=Question.objects.get(id_ques=question_id)
	serializer=QuestionSerializer(question1)
	
	
	return Response(serializer.data)
@api_view(['POST'])
@permission_classes((IsAuthenticated, ))
def answer_v(request):
	serializer= AnswerSerializer(data=request.data)
	if serializer.is_valid():
		answer=serializer.validated_data['ans']
		ques_id=int(serializer.validated_data['id_ques'])
		ques=Question.objects.get(id_ques=ques_id)
		if answer==ques.ans :
			user=request.user
			team=Teams.objects.get(user=user)
			team.question_attempted=team.question_attempted+1
			team.save(update_fields=['question_attempted'])
			ques=Question.objects.get(id_ques=ques_id)
			j=questions_attempt.objects.create(Team=team,ques_id=ques)
			j.Team=team
			j.ques_id=ques
			j.save()
			return redirect('question')
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
@api_view(['GET'])
@permission_classes((IsAuthenticated, ))
def profile_v(request):
	user=request.user
	profile=Teams.objects.get(user=user)
	profile_serializer=TeamSerializer(profile)
	
	return Response(profile_serializer.data)
	
	
