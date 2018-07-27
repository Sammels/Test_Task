from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from django.views.decorators.csrf import csrf_exempt
from rest_framework.renderers import JSONRenderer
from rest_framework.parsers import JSONParser
from testing_apps.models import Point, Point_type
from testing_apps.serializers import PointSerializer, Point_typeSerializer

# Create your views here.
@csrf_exempt
def testing_apps_list(request):
    
    if request.method == 'GET':
        testing_apps_point = Point.objects.all()
        testing_apps_point_type = Point_type.objects.all()
        point_serializer = PointSerializer(testing_apps, many=True)
        point_type_serializer = Point_typeSerializer(testing_apps, many=True)
        return JsonResponse(point_serializer.data, point_type_serializer.data, safe=False)

    elif request.method == 'POST':
        data = JSONParser().parse(request)
        point_serializer = PointSerializer(data=data)
        point_type_serializer = Point_typeSerializer(data=data

        if point_serializer.is_valid() and point_type_serializer.is_valid() :
            point_serializer.save()
            point_type_serializer.save()
            return JsonResponse(point_serializer.data, status=201), JsonResponse(point_type_serializer.data, status=201)
        return JsonResponse(point_serializer.errors, status=400), JsonResponse(point_type_serializer.errors, status=400)

@csrf_exempt
def testing_apps_detail(request, pk):
   
    try:
        testing_apps_point = Point.objects.get(pk=pk)
    except Point.DoesNotExist:
        return HttpResponse(status=404)

    try:
        testing_apps_point_type = Point_type.objects.get(pk=pk)
    except Point_type.DoesNotExist:
        return HttpResponse(status=404)

    if request.method == 'GET':
        point_serializer = PointSerializer(testing_apps_point)
        point_type_serializer  = Point_typeSerializer(testing_apps_point_type)
        return JsonResponse(testing_apps_point.data), JsonResponse(testing_apps_point_type.data)

    elif request.method == 'PUT':
        data = JSONParser().parse(request)
        point_serializer = PointSerializer(testing_apps_point, data=data)
        point_type_serializer = Point_typeSerializer(testing_apps_point_type, data=data)
        if point_serializer.is_valid() and point_type_serializer.os_valid():
            point_serializer.save()
            point_type_serializer.save()
            return JsonResponse(point_serializer.data), JsonResponse(point_type_serializer.data)
        return JsonResponse(point_serializer.errors, status=400), JsonResponse(point_type_serializer.errors, status=400)

    elif request.method == 'DELETE':
        testing_apps_point.delete()
        testing_apps_point_type.delete()
        return HttpResponse(status=204)
