from django.conf.urls import url
from testing_apps import views

urlpatterns = [
    url(r'^testing_apps/$', views.testing_apps_list),
    url(r'^testing_apps/(?P<pk>[0-9]+)/$', views.testing_apps_detail),
]
