from testing_apps.models import Point, Point_type
from rest_framework import serializers


class PointSerializer(serializers.ModelSerializer):
    class Meta:
        model = Point
        fields = ('pnt_name', 'pnt_code', 'pnt_adress', 'latitude', 'longitude')

##    pnt_name = serializers.CharField(required=False,
##                                         allow_blank=True,
##                                         max_length=100)
##
##    pnt_code = serializers.CharField(required=False,
##                                         allow_blank=True,
##                                         max_length=100)
##
##    pnt_adress = serializers.CharField(required=False,
##                                         allow_blank=True,
##                                         max_length=100)
##
##    latitude = serializers.DecimalField(max_digits=19,
##                                            decimal_places=10)
##
##    longitude = serializers.DecimalField(max_digits=19,
##                                            decimal_places=10)

    def create(self, validated_data):
        return testing_apps.objects.create(**validated_data)


    def update(self, instance, validated_data):
        instance.pnt_name = validated_data.get('Имя точки', instance.pnt_name)
        instance.pnt_code = validated_data.get('Код точки', instance.pnt_code)
        instance.pnt_adress = validated_data.get('Адрес точки', instance.pnt_adress)
        instance.latitude = validated_data.get('Широта', instance.latitude)
        instance.longitude = validated_data.get('Долгота', instance.longitude)
        instance.save()
        return instance


class Point_typeSerializer(serializers.Serializer):
    class Meta:
        model = Point_type
        fields = ('type_name', 'type_description')


##    type_name = serializers.CharField(required=False,
##                                      allow_blank=True,
##                                      max_length=100)
##
##    type_description = serializers.CharField(required=False,
##                                             allow_blank=True,
##                                             max_length=100)
