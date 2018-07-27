from django.db import models
from django.utils.translation import ugettext_lazy as _


class Point(models.Model):
    pnt_name = models.CharField(max_length=30, help_text=_('Имя точки'))
    pnt_code = models.CharField(max_length=30, help_text=_('Код точки'))
    pnt_adress = models.CharField(max_length=30, help_text=_('Адрес точки'))

##  
##    pnt_typed = models.ForeignKey(Point_type,
##                                  on_delete=models.CASCADE,
##                                  related_name='Тип точки',
##                                  verbose_name=_('Тип точки'),
##                                  )

    latitude = models.DecimalField(max_digits=5, decimal_places=2,
                                  help_text=_('Широта'))

    longitude = models.DecimalField(max_digits=5, decimal_places=2,
                                  help_text=_('Долгота'))


class Point_type(models.Model):
    type_name = models.CharField(max_length=200, help_text=_('Имя типа') )
    type_description = models.CharField(max_length=200, help_text=_('Описание'))
