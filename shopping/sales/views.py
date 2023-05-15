from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse
# 导入 Customer
from common.models import Commodity
from django.http import JsonResponse
from rest_framework.views import APIView  # API
from rest_framework.response import Response  # 返回
from django.db.models import Q
from sales.serializers import *		# 导app名.序列化器
import json


# def listgoods(request):
#
#     # 返回一个QuerySet对象 ，包含所有的表记录
#     qs = Commodity.objects.values()
#
#     # 将QuerySet对象转化为list类型
#     # 否则不能被转化为JSON字符串
#     retlist = list(qs)
#
#     return JsonResponse({'ret': 0, 'retlist': retlist})


class SearchAPIView(APIView):
    def get(self, request):

        # sc = request.GET.get('search', None)
        text = request.GET.get('text')

        # context = None

        # if sc:
        #    print(sc)
        # if text:
        #    print(text)

        # goods = Commodity.objects.filter(Q(name__icontains=sc) | Q(cate__name__contains=sc))
        goods = Commodity.objects.filter(Q(name__icontains=text))

        # context = {'goods': goods}
        ser = GoodsModelSerializer(goods, many=True)

        # return render(request, 'goods.html', context)
        return Response(ser.data)