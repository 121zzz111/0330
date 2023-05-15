from rest_framework.serializers import ModelSerializer
from common.models import *


class GoodsModelSerializer(ModelSerializer):
    class Meta:
        model = Commodity
        fields = '__all__'

