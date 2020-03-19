import re
import requests

login = 'https://sso.shisu.edu.cn/sso/login'

header = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.132 Safari/537.36',
}

s = requests.session()
req = s.get(login)
lt = re.findall(r'(LT-.*?-sso.shisu.edu.cn)', req.text, re.S | re.M)[0]
exeution = re.findall(r'name="execution" value="(.*?)"', req.text, re.S | re.M)[0]

data = {
                  'lt' : lt,
                  'execution' : exeution,
                  '_eventId' : 'submit',
                  'authType' : 'pwd',
                  'isShowRandomCode' : '0',
                  'un' : #username,
                  'pd' : #password,
}

s.post(login, data=data, headers=header)