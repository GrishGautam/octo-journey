from django.urls import include, path
from . import views


urlpatterns = [
    path('', views.index, name = 'index'),
    path('ok', views.blank, name = 'blank'),
    path('weather', views.weather, name = 'weather'),

]
