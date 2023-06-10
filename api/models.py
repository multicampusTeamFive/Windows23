from django.db import models

class ODFineDust(models.Model):       # 실외 미세먼지 
    value = models.FloatField() 
    date = models.DateTimeField() 
    # 미세먼지 좋음/보통/나쁨 grade는 value가지고 안드로이드에서 처리하는 걸로


class ODUltraFineDust(models.Model):       # 실외 초미세먼지 
    value = models.FloatField() 
    date = models.DateTimeField() 


class IDFineDust(models.Model):       # 실내 미세먼지 
    place = models.CharField(max_length = 50)
    value = models.FloatField() 
    date = models.DateTimeField() 


class IDUltraFineDust(models.Model):       # 실내 초미세먼지 
    value = models.FloatField() 
    date = models.DateTimeField() 


class Temp(models.Model):     # 실외 온도
    value = models.FloatField() 
    date = models.DateTimeField() 


class Rain(models.Model):    # 비가 오는지 안오는지
    rainstatus = models.BooleanField(default = False)


class WindowStatus(models.Model):     # 창문 개폐 상태
    windowstatus = models.BooleanField(default = False)