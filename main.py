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
import checksendNotify

session = requests.session()
# 机场的地址
url = os.environ.get('JC_URL')
# 配置用户名（一般是邮箱）
email = os.environ.get('JC_EMAIL')
# 配置用户名对应的密码 和上面的email对应上
passwd = os.environ.get('JC_PASSWD')

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
    print('登录失败，请检查网络或参数')   

# 签到
print('进行签到..'+check_url)

try:          
    result = json.loads(session.post(url=check_url,headers=header).text)
    print(result['msg'])
    content = result['msg']
    
    # 推送
    checksendNotify.send(url+"签到成功", content)
except:
    print('签到失败，检查URL、用户密码！')
    
