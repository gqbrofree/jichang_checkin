#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
File: main.py(机场通用签到)
Author: gqbrofree
cron: 0 40 12 * * *
new Env('机场通用签到');
Update: 2023/8/31
"""


import requests, json, re, os, json

session = requests.session()
# 机场的地址
url = os.environ.get('URL')
# 配置用户名（一般是邮箱）
email = os.environ.get('EMAIL')
# 配置用户名对应的密码 和上面的email对应上
passwd = os.environ.get('PASSWD')
# server酱
SCKEY = os.environ.get('SCKEY')

login_url = '{}/auth/login'.format(url)
check_url = '{}/user/checkin'.format(url)


header = {
        'refere': login_url,       
        'origin': url,
        'user-agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/86.0.4240.75 Safari/537.36',
        'content-type':'application/json;charset=UTF-8'
}
data = {
        'email': email,
        'passwd': passwd,
        'code': '', 
        'remember_me': False
}


#进行登录

print('进行登录..'+login_url)


try:       

    response = json.loads(session.post(url=login_url,headers=header,data=json.dumps(data)).text) 
        
    print(response['msg'])

except:
    print('录失败，请检查网络或参数')   

# 进行签到
print('进行签到..'+check_url)


try:
          

    result = json.loads(session.post(url=check_url,headers=header).text)
    print(result['msg'])
    content = result['msg']
       
    # 进行推送
    if SCKEY != '':
        push_url = 'https://sctapi.ftqq.com/{}.send?title=机场签到&desp={}'.format(SCKEY, content)
        requests.post(url=push_url)
        print('推送成功')
except:
    content = '签到失败'
    print(content)
    if SCKEY != '':
        push_url = 'https://sctapi.ftqq.com/{}.send?title=机场签到&desp={}'.format(SCKEY, content)
        requests.post(url=push_url)
