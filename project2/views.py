from django.http import JsonResponse
from django.http import HttpResponse
from numpy import False_
from requests import Response
from .models import Nokta, user
from .serializers import noktaSerializer, userSerializer
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status


@api_view(['GET','POST'])
def user_list(request):
    
    if request.method == 'GET':
        users = user.objects.all()
        serializer = userSerializer(users,many=True)
        return JsonResponse(serializer.data, safe = False)
    if request.method == 'POST':
        serializer = userSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            data = serializer.data
            return Response(data, status = status.HTTP_201_CREATED)
        
@api_view(['GET','PUT'])
def nokta_list(request):
    if request.method == 'GET':
        nokta = Nokta.objects.all()
        serializer = noktaSerializer(nokta,many=True)
        return JsonResponse(serializer.data,safe=False)
    if request.method == 'PUT':
        pass    