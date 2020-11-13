from django.shortcuts import render
from django.http import HttpResponse,JsonResponse
from .models import Register
from .serializers import RegisterSerializer
from rest_framework.parsers import JSONParser
from django.views.decorators.csrf import csrf_exempt
# Create your views here.



@csrf_exempt
def user_list(request):
    if request.method == 'GET':
        query_set = Register.objects.all()
        serializer = RegisterSerializer(query_set, many=True)
        return JsonResponse(serializer.data, safe=False)

    elif request.method == 'POST':
        data = JSONParser().parse(request)
        serializer = RegisterSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data, status=200)
        return JsonResponse(serializer.errors, status=400)


@csrf_exempt
def login(request):
    if request.method == 'POST':
        data=JSONParser().parse(request)
        search_name = data['useremail']
        obj=Register.objects.get(useremail=search_name)

        if data['userpw'] == obj.userpw:
            return HttpResponse(status=200)
        else:
            return HttpResponse(status=400)
        