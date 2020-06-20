import requests

if __name__ == '__main__':
    # target = "http://www.baidu.com"
    # req = requests.get(url=target)
    # print(req)  # 返回对象
    # print(req.text)  # 返回响应内容
    # print(req.content)  # 二进制文本流
    # print(req.content.decode('utf-8'))
    # print(req.headers)  # 响应的头信息
    # print(req.url)  # 请求的url地址
    # print(req.status_code)  # 请求的状态码，404就是错误
    # print(req.request.headers)  # 请求的头信息

    # url = 'https://www.lmonkey.com/'
    url = 'https://www.xicidaili.com/nn'
    # 定义请求头信息
    header = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/78.0.3904.108 Safari/537.36'
    }

    res = requests.get(url=url, headers = header)

    code = res.status_code
    print(code)

    if code == 200:
        with open('./test.html','w', encoding='utf-8') as fp:
            fp.write(res.text)