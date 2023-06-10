from rest_framework import routers 
from .views import *
from django.urls import path, include
from .views import *

router = routers.DefaultRouter()

# 미세먼지
router.register('outdoor_finedust', ODFineDustViewSet)
router.register('out_ultrafinedust', ODUltraFineDustViewSet)
router.register('indoor_finedust', IDFineDustViewSet)
router.register('in_ultrafinedust', IDUltraFineDustViewSet)

router.register('temp', TempViewSet)
router.register('rain', RainViewSet)
router.register('window', WindowViewSet)

app_name = 'api'

urlpatterns = [ 
    path('', include(router.urls)),
]
