# 网站将cookie返回到用户浏览器，以确认是否为当前用户继续方位网站
# 用户第二次发送请求时，将cookie和请求一同发送给服务器
# cookie不安全，不能记录敏感信息
# session将信息记录在服务器，通过cookie将信息提交给session，通过sessionID完成对用户的识别

import requests

# 定义url

url = 'http://bi-si777.xyz/forum.php'

headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/78.0.3904.108 Safari/537.36'
    , 'cookie': 'Ovo6_2132_saltkey=nOFRcgPc; Ovo6_2132_lastvisit=1575717691; PHPSESSID=kic4feapcoumierjua0kiphv80; Ovo6_2132_sendmail=1; Ovo6_2132_ulastactivity=1575721344%7C0; Ovo6_2132_auth=f3c3bWjlhyAIBibzbGWcmKTIO6zBWtrRdyOpnfSSqw18Ws9lOuVHtJPjfRn7%2B0V70Hsq3qvck2jHZ453PfEVUXj%2FnJWB; Ovo6_2132_creditnotice=0D0D2D0D0D0D0D0D0D2297663; Ovo6_2132_creditbase=0D21D134D0D0D0D0D0D0; Ovo6_2132_creditrule=%E6%AF%8F%E5%A4%A9%E7%99%BB%E9%8C%84; Ovo6_2132_lastcheckfeed=2297663%7C1575721344; Ovo6_2132_checkfollow=1; Ovo6_2132_lastact=1575721344%09forum.php%09; Ovo6_2132_nofavfid=1; Ovo6_2132_myrepeat_rr=R0'
}

# 定义cookie

# cookie = 'Ovo6_2132_saltkey=nOFRcgPc; Ovo6_2132_lastvisit=1575717691; PHPSESSID=kic4feapcoumierjua0kiphv80; Ovo6_2132_sendmail=1; Ovo6_2132_ulastactivity=1575721344%7C0; Ovo6_2132_auth=f3c3bWjlhyAIBibzbGWcmKTIO6zBWtrRdyOpnfSSqw18Ws9lOuVHtJPjfRn7%2B0V70Hsq3qvck2jHZ453PfEVUXj%2FnJWB; Ovo6_2132_creditnotice=0D0D2D0D0D0D0D0D0D2297663; Ovo6_2132_creditbase=0D21D134D0D0D0D0D0D0; Ovo6_2132_creditrule=%E6%AF%8F%E5%A4%A9%E7%99%BB%E9%8C%84; Ovo6_2132_lastcheckfeed=2297663%7C1575721344; Ovo6_2132_checkfollow=1; Ovo6_2132_lastact=1575721344%09forum.php%09; Ovo6_2132_nofavfid=1; Ovo6_2132_myrepeat_rr=R0'

req = requests.get(url=url,headers=headers)

print(req.status_code)
print(req.text)
