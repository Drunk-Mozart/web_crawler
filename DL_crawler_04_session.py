# 下面这个代码现在用不了了

import requests

# 定义url

url = 'http://bi-si777.xyz/forum.php'
loginurl = 'http://www.zmz2019.com/User/Login/ajaxLogin'

headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/78.0.3904.108 Safari/537.36'
}

req = requests.session()

data = {
    'account': 'yichuan@itxdl.cn',
    'password': 'pyTHON123',
    'remember': '1',
    'urluback': 'http://wwww.zmz2019.com/user/user'
}

res = req.post(url=loginurl, headers=headers,data=data)

print(res.status_code)
if res.status_code == 200:
    res = req.get(url = url, headers=headers)
    print(res.text)
