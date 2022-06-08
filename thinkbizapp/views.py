from django.shortcuts import render
from . models import *
from thinkbizapp.serializers import educators
from django.http.response import JsonResponse
from rest_framework.parsers import JSONParser
from django.views.decorators.csrf import csrf_exempt


# Create your views here.
@csrf_exempt
def educator(request,id=0):
    if request.method=='GET':
        educator_datas = Educator.objects.all()
        serializer_data = educators(educator_datas, many=True)
        return JsonResponse(serializer_data.data, safe=False)


    elif request.method=='POST':
        educator_datas = JSONParser().parse(request)
        serlzerdata = educators(data=educator_datas)
        if serlzerdata.is_valid():
            serlzerdata.save()
            return JsonResponse('Data inserted succesfully', safe=False)
        return JsonResponse('An error occured', safe=False)

    elif request.method=='DELETE':
        deldatae = Educator.objects.get(id=id)
        deldatae.delete()
        return JsonResponse('data deleted' ,safe=False)
        
    elif request.method=='PUT':
        educator_datas = JSONParser().parse(request)
        user = Educator.objects.get(id=educator_datas['id'])
        serializerdata = Educator(user,educator_datas)
        if serializerdata.is_valid():
            serializerdata.save()
            return JsonResponse('Data updated succesfully', safe=False)
        return JsonResponse('Failed to Update', safe=False)