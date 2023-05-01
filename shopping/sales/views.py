from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse
# 导入 Customer
from common.models import Commodity
from django.http import JsonResponse
from django.db.models import Q
import json

def listgoods(request):
    # 返回一个QuerySet对象 ，包含所有的表记录
    qs = Commodity.objects.values()

    # 将QuerySet对象转化为list类型
    # 否则不能被转化为JSON字符串
    retlist = list(qs)

    return JsonResponse({'ret': 0, 'retlist': retlist})


def search(request):
    sc = request.GET.get('search', None)

    context = None

    if sc:
        print(sc)

        goods = Commodity.objects.filter(Q(name__icontains=sc))

        context = {'goods': goods}

    return render(request, 'goods.html', context)
