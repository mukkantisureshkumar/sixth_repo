from django.urls import path
from drinks.views import *

app_name='drinks'

urlpatterns=[
    path('teachers/',teachers,name='teachers'),
    path('redwine/',redwine,name='redwine'),
]