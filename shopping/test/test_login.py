# 登录系统测试
import requests, pprint

payload = {
    'username': 'zxz',
    'password': 'bb88014'
}

response = requests.post('http://localhost/api/mgr/signin',
                         data=payload)

pprint.pprint(response.json())