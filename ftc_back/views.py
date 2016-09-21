from django.shortcuts import render,redirect
from django.http import HttpResponse
from rest_framework import generics
from ftc_back.models import Question,Teams,questions_attempt,Clues,Tries
from ftc_back.serializers import AnswerSerializer,TeamSerializer,ClueSerializer,AuthTokenSerializer,Question_getSerializer,Team_createSerializer
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.decorators import api_view, permission_classes
from django.views.decorators.csrf import csrf_exempt
from rest_framework.permissions import IsAuthenticated
import math,random
from rest_framework import parsers, renderers
from rest_framework.authtoken.models import Token
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.views import exception_handler




@api_view(['POST'])
@permission_classes((IsAuthenticated, ))
def Question_v(request):
	user=request.user
	team=Teams.objects.get(user=user)
	question=Question_getSerializer(data=request.data)
	if question.is_valid():
		question_id=question.validated_data['questionid']
	
	
	question1=Question.objects.get(questionid=question_id)
	
	resp={"question":question1.question}
	
	
	return Response(resp)

@api_view(['POST'])
@permission_classes((IsAuthenticated, ))
def answer_v(request):
	serializer= AnswerSerializer(data=request.data)
	if serializer.is_valid():
		answer=serializer.validated_data['answer']
		ques_id=int(serializer.validated_data['questionid'])
		ques=Question.objects.get(questionid=ques_id)
		if answer==ques.answer :
			user=request.user
			team=Teams.objects.get(user=user)
			team.question_attempted=team.question_attempted+1
			team.save(update_fields=['question_attempted'])
			ques=Question.objects.get(questionid=ques_id)
			j=questions_attempt.objects.create(Team=team,ques_id=ques)
			j.Team=team
			j.ques_id=ques
			j.save()
			clue=Clues.objects.get(clue_question__questionid=ques_id)
			question_attempt_list=[]
			question_list_all=[]
			try :
				q1=questions_attempt.objects.filter(Team=team)
				for i in q1:
							question_attempt_list.append(i.ques_id.questionid)
			except TypeError:
				pass
	
	
			question=Question.objects.filter(level=team.level)
			for j in question:
				question_list_all.append(j.questionid)
			final_list=set(question_list_all)-set(question_attempt_list)
			final_list=list(final_list)
			if len(final_list)==0:
				level_end=Question.objects.get(questionid=114)
				level_result={'success':'true','clue':clue.clue_id,'questionid':level_end.questionid,'question':level_end.question,'lat':clue.clue_lt,'long':clue.clue_ln,'alphabet':clue.clue_alphabet} #clue questionid question lat lng letter

				
				
				return Response(level_result)
			index=len(final_list)-1
			if index >=0 :
							index=random.randint(0,index)
			else:
							index=index+1
			question_id=final_list[index]
			questions=Question.objects.get(questionid=question_id)
			
			clue_result={'success':'true','clue':clue.clue_id,'questionid':question_id,'question':questions.question,'lat':clue.clue_lt,'long':clue.clue_ln,'letter':clue.clue_alphabet} #clue questionid question lat lng letter
			
			return Response(clue_result)
		else:
			
			
			user=request.user
			team=Teams.objects.get(user=user)
			
			try:
				obj=Tries.objects.get(Teams=team)

			except Tries.DoesNotExist:
    			
    								obj = Tries.objects.create(Teams=team,Attempts=0)
    								obj.save()
    		obj.Attempts+=1
    		obj.save()

        return Response({"success":"false","message":"Wrong answer"})
@api_view(['GET'])

def profile_v(request):
	
	profile=Teams.objects.all().order_by('-question_attempted','tries__Attempts')
	profile_serializer=TeamSerializer(profile,many=True)
	#l=[{"admin":"hitesh"},{"admin2":"hitesh2"}]
	#l={"list":l}
	return Response(profile_serializer.data)
	
@permission_classes((IsAuthenticated, ))
@api_view(['POST'])	
def location_check(request):
	serializer=ClueSerializer(data=request.data)
	if serializer.is_valid():
		clueid=serializer.validated_data['clue_id']
		lat1=serializer.validated_data['clue_lt']
		lon1=serializer.validated_data['clue_ln']
		clue=Clues.objects.get(clue_id=clueid)
		R=6371
		lat2=clue.clue_lt
		lon2=clue.clue_ln
		dlat=(lat2-lat1)*math.pi/180
		dlon=(lon2-lon1)*math.pi/180
		a=math.sin(dlat/2)*math.sin(dlat/2)+math.cos(lat1*math.pi/180)*math.cos(lat2*math.pi/180)*math.sin(dlon/2)*math.sin(dlon/2)
		c=2*math.atan2(math.sqrt(a),math.sqrt(1-a))
		d=R*c
		d=d*1000
		bad={"Clue":clueid,"message":"Not in location"}
		if (d<=100):
			
			return redirect('question')
		else:
			return Response(bad)
		
		
	from rest_framework_jwt.views import ObtainJSONWebToken



class ObtainAuthToken(APIView):
    throttle_classes = ()
    permission_classes = ()
    parser_classes = (parsers.FormParser, parsers.MultiPartParser, parsers.JSONParser,)
    renderer_classes = (renderers.JSONRenderer,)
    serializer_class = AuthTokenSerializer

    def post(self, request, *args, **kwargs):
        serializer = AuthTokenSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = serializer.validated_data['user']
        if user=='null':
        	return Response({'success':'false','message':'Invalid Crediantials'})
        token, created = Token.objects.get_or_create(user=user)
        return Response({'success':'true','authtoken': token.key,'questionid':1,'question':'What the Fork ?'}) #success authtoken quesitionid question
		

obtain_auth = ObtainAuthToken.as_view()
@permission_classes((IsAuthenticated, ))
@api_view(['POST'])	
def  Team_upadte(request):
	user=request.user
	team=Team_createSerializer(data=request.data)
	if team.is_valid():
		team_name=team.validated_data['name']
	try:
				obj=Teams.objects.get(name=team_name)
				return Response({'success':'false','message':'Team already exists'})
	except Teams.DoesNotExist:
	
		
			
				obj=Teams.objects.create(user=user,name=team_name)
	
				obj.save()
	return Response({"success":"true","message":"Team created"})
		
