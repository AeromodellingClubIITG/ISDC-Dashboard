from django.urls import path
from . import views


urlpatterns = [
    path('', views.index, name='index'),
    path('video_feed/', views.video_feed, name='video_feed'),
    path('get_sensor_data/', views.get_sensor_data, name='get_sensor_data'),
]
