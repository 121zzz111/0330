# 查看商品信息测试

import requests,pprint

response = requests.get('http://localhost/api/sales/goods')

pprint.pprint(response.json())