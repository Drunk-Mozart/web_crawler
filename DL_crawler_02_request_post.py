# 用post方法，返回请求
import requests

# 定义url

url = 'https://fanyi.baidu.com/sug'

headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/78.0.3904.108 Safari/537.36'
}

data = {'kw': '你好'}
res = requests.post(url=url, headers=headers, data=data)
code = res.status_code
if code == 200:
    print("请求成功")
    data = res.json()
    if data['errno'] == 0:
        print('响应成功')
        print(data['data'][0]['k'])
        print(data['data'][0]['v'][-6:-1])

    # print(res.text)
    print(res.json())
