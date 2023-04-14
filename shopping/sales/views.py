from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse
# 导入 Customer
from common.models import Commodity
from django.http import JsonResponse
import json

def listgoods(request):
    # 返回一个QuerySet对象 ，包含所有的表记录
    qs = Commodity.objects.values()

    # 将QuerySet对象转化为list类型
    # 否则不能被转化为JSON字符串
    retlist = list(qs)

    return JsonResponse({'ret': 0, 'retlist': retlist})