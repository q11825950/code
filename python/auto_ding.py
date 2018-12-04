#coding=utf8

import requests
import re

#登录豆瓣网站通过浏览器获取
cookie = 'll="108296"; bid=A15UCrHkbU4; _ga=GA1.2.1646425546.1520868371; _vwo_uuid_v2=D9259AAD7CAD23C91CF5B0925770B2D45|bfcc908c735a139e1738583d2e90b2de; gr_user_id=9c1d1d6b-87ec-4ff4-81c4-0a779721a18f; ue="lwhyx9@qq.com"; OUTFOX_SEARCH_USER_ID_NCOO=328889871.89926124; __utmv=30149280.1466; douban-fav-remind=1; __yadk_uid=JflylLEQXpoB2MAKaVY29uSc5suFHgDx; viewed="27032786_30155726_26786719_3369600_6538430"; __utmc=30149280; __utmz=30149280.1543833505.24.17.utmcsr=google|utmccn=(organic)|utmcmd=organic|utmctr=(not%20provided); dbcl2="14660354:s4KguRhVhyk"; ck=WE2G; push_noty_num=0; push_doumail_num=0; ap_v=0,6.0; _pk_ref.100001.8cb4=%5B%22%22%2C%22%22%2C1543892388%2C%22https%3A%2F%2Fwww.google.com.hk%2F%22%5D; _pk_ses.100001.8cb4=*; __utma=30149280.1646425546.1520868371.1543833505.1543892389.25; _pk_id.100001.8cb4=653f1061c8391114.1527506463.144.1543893858.1539231911.; __utmt=1; __utmb=30149280.48.7.1543892925721'
#小组贴的url
baseurl = 'https://www.douban.com/group/topic/129019947/'
url = baseurl + 'add_comment'

header = {
    'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_13_4) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/66.0.3359.181 Safari/537.36',
    'Cookie': cookie
}

rval = requests.get(baseurl + '?start=5000#last', headers=header)
#检验是否需要输入验证码
mat = re.search('src=\"(.*?captcha.*?)\"', rval.text)
if mat:
    print "不识别验证码，退出程序"
else:
    data = {
        "rv_comment": 'ding',
        "ck": "aubV",
        'start': '0',
        'submit_btn': '加上去'
    }
    rval = requests.post(url=url, data=data, headers=header)
    print rval
    print '自动顶帖'
