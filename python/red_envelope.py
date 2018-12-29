#!/usr/bin/python
# -*- coding: UTF-8 -*-
import random
import time
import subprocess

import requests
import logging

logging.basicConfig(level=logging.INFO, format='%(asctime)s.%(msecs)03d %(levelname)s: %(message)s',
                    datefmt='%Y-%m-%d %H:%M:%S')


def red_envelope(n):
    url = "https://h5.ele.me/restapi/member/v1/users/68477837/sign_in/limit/hongbao"
    cookie = 'ubt_ssid=z52ui6b3jnr48epn9s4m8rkzk4omb7gk_2018-03-27; _utrace=d8a4cafbd5a0b2dbeb9e04c86247bc25_2018-03-27; perf_ssid=cdv2xytahlxm9hqr9whe9ckkjmj1i43q_2018-04-08; quizer_uuid=prec1w9qrnn6g5x22hjzb1xzk6qqr7hh_2018-05-23; OUTFOX_SEARCH_USER_ID_NCOO=381339675.42863226; cna=licpE7was00CAdr1Q/wI9+P/; track_id=1543334781|16800d3b697bd419d410b8255df1e30b0796659f1f54fedfd0|9696e3f9e47e677287fef13b2063758a; COFFEE_BETA_TOKEN=e3a2d617-199c-482e-9283-34794f8df8aa; USERID=68477837; UTUSER=68477837; SID=Qs1qyHfdoIy9zGT1HwpRQcoe5934ZhyEqQmw; COFFEE_PROD_TOKEN=ebaead5b-2203-4662-9592-3673d8132823; COFFEE_TOKEN=ebaead5b-2203-4662-9592-3673d8132823; ___rl__test__cookies=1545841873441; isg=BCsr-OzR81EFVijb5oM2crvtuknV6BRpDqs1fp2oBmrCPEqeJRKfFireknpSHJe6'
    agent = "Rajax/1 Apple/iPhone7,1 iOS/12.1 Eleme/8.5.1 ID/3B0EE632-2E54-45F8-953F-6FB9AB9F8889; IsJailbroken/0 ASI/71CA293E-5FF6-4267-9954-D44BC8E3984E Mozilla/5.0 (iPhone; CPU iPhone OS 12_1 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Mobile/16B92 AliApp(ELMC/8.5.1)"
    headers = {
        'User-agent': agent,
        "Cookie": cookie
    }
    data = {
        "user_id": 68477837,
        "latitude": 31.232949,
        "longitude": 121.382249
    }
    i = 0
    time.sleep(56.76)
    while i < n:
        i = i + 1
        response = requests.post(url, data, headers=headers)
        logging.info(str(response.status_code) + " " + response.content)


if __name__ == '__main__':
    n = 7
    red_envelope(n)
    path = "/root/ele.log"
    sp_tail_file = subprocess.Popen(["tail", "-" + str(n), path], stdout=subprocess.PIPE)
    tail_output = sp_tail_file.communicate()[0]
    url = "https://sc.ftqq.com/SCU37167T460e639bc3f6f62ab90c3a551460553d5c090f360cef6.send?text=ele_red_envelope:" + \
          str(random.randint(0, 1000)) + "&desp=" + tail_output
    requests.post(url)
