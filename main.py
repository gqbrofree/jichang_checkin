import requests, json, re, os

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
        'origin': url,
        'user-agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/86.0.4240.75 Safari/537.36'
}
data = {
        'email': email,
        'passwd': passwd,
        'code': '', 
        'remember_me': 1
}


#进行登录

try:
        checkin = requests.post(checkin_url,headers={
            'cookie': cookie ,
            'referer': referer,
            'origin':origin,
            'user-agent':useragent,
            'content-type':'application/json;charset=UTF-8'},data=json.dumps(payload))
        state =  requests.get(state_url,headers={
            'cookie': cookie ,
            'referer': referer,
            'origin':origin,
            'user-agent':useragent})
    except Exception as e:
        print(f"签到失败，请检查网络：{e}")
        return None, None, None
    





try:
    #进行登录
    print('进行登录...' + login_url)
    #response = json.loads(session.post(url=login_url,headers=header,data=data).text)
    print(response['msg'])
        
    # 进行签到
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
