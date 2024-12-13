import json
import re

import requests

cookies = {
    'websitepoptg_api_time': '1733899768072',
    'qgqp_b_id': 'b69337736fc6a2bdb75e3e7172b3fa2d',
    'st_si': '48011885781322',
    'st_asi': 'delete',
    'st_pvi': '97679559614289',
    'st_sp': '2024-12-11%2014%3A49%3A28',
    'st_inirUrl': 'https%3A%2F%2Fwww.google.com%2F',
    'st_sn': '4',
    'st_psi': '20241211145211218-113200301321-1475792611',
}

headers = {
    'Host': '25.push2.eastmoney.com',
    'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/131.0.0.0 Safari/537.36',
    'Accept': '*/*',
    'Referer': 'http://quote.eastmoney.com/center/boardlist.html',
    'Accept-Language': 'zh-CN,zh;q=0.9',
    # 'Cookie': 'websitepoptg_api_time=1733899768072; qgqp_b_id=b69337736fc6a2bdb75e3e7172b3fa2d; st_si=48011885781322; st_asi=delete; st_pvi=97679559614289; st_sp=2024-12-11%2014%3A49%3A28; st_inirUrl=https%3A%2F%2Fwww.google.com%2F; st_sn=4; st_psi=20241211145211218-113200301321-1475792611',
}


params = {
    'cb': 'jQuery112407059149081674101_1733899929809',
    'pn': '3',
    'pz': '20',
    'po': '1',
    'np': '1',
    'ut': 'bd1d9ddb04089700cf9c27f6f7426281',
    'fltt': '2',
    'invt': '2',
    'dect': '1',
    'wbp2u': '|0|0|0|web',
    'fid': 'f3',
    'fs': 'b:BK0707+f:!50',
    'fields': 'f1,f2,f3,f4,f5,f6,f7,f8,f9,f10,f12,f13,f14,f15,f16,f17,f18,f20,f21,f23,f24,f25,f22,f11,f62,f128,f136,f115,f152,f45',
    '_': '1733899929831'
}


response = requests.get(
    'http://25.push2.eastmoney.com/api/qt/clist/get',
    params=params,
    cookies=cookies,
    headers=headers,
)
result = response.text

matches = re.match(r'jQuery\d+_\d+\((.*)\)', result).group(1)
result_json = json.loads(matches)

print(result_json)
