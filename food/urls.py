from django.urls import path
from food.views import *

app_name='food'

urlpatterns=[
    path('hott/',hott,name='hott'),
    path('sweet/',sweet,name='sweet'),
]