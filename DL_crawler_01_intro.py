import requests

if __name__ == '__main__':
    target = "http://www.baidu.com"
    req = requests.get(url = target)
    print(req)
    print(req.text)