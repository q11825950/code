#!/usr/bin/python
# -*- coding: UTF-8 -*-
import requests
import logging
import os
import sys
import codecs
import threading
import datetime
import time
# sys.setdefaultencoding('utf-8')
time_now = datetime.datetime.now().strftime('%H:%M:%S.%f')

logging.basicConfig(level=logging.INFO,
                    format='%(asctime)s %(filename)s[line:%(lineno)d] %(levelname)s %(message)s',
                    datefmt='%a, %d %b %Y %H:%M:%S',
                    # filename=os.path.dirname(__file__)+'/elem.log',
                    filemode='a')

logging.info("start time"+time_now)


def hongbao():
    cookie = {'SID': 'pAS2ka6rZg7YKuUq5R4PbnL4KDG08dOgKFBA', ' USERID': '68477837',
              ' isg': 'BF9fZziveOvWNXz3iocqVk8x7rUpbLMJqXhwK_GsC45EgHsC6JYDt8ERRxD-KIve',
              ' track_id': '1543334781|16800d3b697bd419d410b8255df1e30b0796659f1f54fedfd0|9696e3f9e47e677287fef13b2063758a',
              ' _utrace': 'd8a4cafbd5a0b2dbeb9e04c86247bc25_2018-03-27', ' cna': 'licpE7was00CAdr1Q/wI9+P/',
              ' ubt_ssid': 'z52ui6b3jnr48epn9s4m8rkzk4omb7gk_2018-03-27',
              ' perf_ssid': 'cdv2xytahlxm9hqr9whe9ckkjmj1i43q_2018-04-08'}
    Agent = "Rajax/1 Apple/iPhone7,1 iOS/12.1 Eleme/8.5.1 ID/3B0EE632-2E54-45F8-953F-6FB9AB9F8889; IsJailbroken/0 ASI/71CA293E-5FF6-4267-9954-D44BC8E3984E Mozilla/5.0 (iPhone; CPU iPhone OS 12_1 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Mobile/16B92 AliApp(ELMC/8.5.1)"

    cookie2 = requests.utils.cookiejar_from_dict(cookie)
    headers = {'User-agent': Agent}
    url2 = "https://h5.ele.me/restapi/member/v1/users/68477837/sign_in/limit/hongbao"
    data = {"user_id": 68477837, "latitude": 31.232949, "longitude": 121.382249}
    n = 0
    time.sleep(57.5)
    while n < 16:
        logging.info(datetime.datetime.now().strftime('%H:%M:%S.%f'))
        n = n + 1
        res2 = requests.post(url2, data, cookies=cookie2, headers=headers)\
            .content.decode('utf-8')
        logging.info(res2)


t = threading.Thread(target=hongbao, name='LoopThread')

t.start()
t.join()
