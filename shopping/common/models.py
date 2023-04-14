from django.db import models

# Create your models here.
class Commodity(models.Model):

    # 商品名称
    name = models.CharField(max_length=200)

    # 商品价格
    price = models.CharField(max_length=200)

    # 剩余数量
    amount = models.CharField(max_length=200)