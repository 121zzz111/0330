# 登录系统测试
import requests, pprint

payload = {
    'username': '85340',
    'password': 'zxz980109'
}

response = requests.post('http://localhost/api/mgr/signin',
                         data=payload)

pprint.pprint(response.json())