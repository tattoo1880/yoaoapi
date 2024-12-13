import time
import hashlib
import requests
import json


def generate_signature_and_url(telephones, key, base_url):
    # 当前时间戳
    timestamp = int(time.time())

    # 模板字符串
    template = (
        "customerTypes=116012874979938888848950,116268519059448888067837"
        "&mobile={}&pageIndex=1&pageSize=10&sort=false&timestamp={}&key={}"
    )

    # 替换模板占位符
    l = template.format(telephones, timestamp, key)

    # 计算 MD5
    md5_hash = hashlib.md5(l.encode('utf-8')).hexdigest().upper()

    # 拼接最终字符串，去掉 &key 部分
    final_l = l + "&signature=" + md5_hash
    final_l = final_l.replace(f"&key={key}", "")

    # 拼接完整的请求 URL
    final_url = f"{base_url}?{final_l}"

    return final_url


# 请求头
headers = {
    'accept': 'application/json, text/plain, */*',
    'accept-language': 'zh-CN',
    'authorization': 'bearer zZ2EqtxhDk4xZK_U9Gw30pKXZZyJnbM-Ydf2j0B2zUf1_z2dwPopanHOO32IN73GFFeJyyGfc4Ghj0BnigbKf8wxvn9M65r31fp0VjIl_X6K3nztw8lRFiatZ443zLY0DgloJvZDSyfG7gvjUHeMVA',
    'origin': 'https://msc.yoao.com',
    'priority': 'u=1, i',
    'sec-ch-ua': '"Google Chrome";v="131", "Chromium";v="131", "Not_A Brand";v="24"',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-platform': '"macOS"',
    'sec-fetch-dest': 'empty',
    'sec-fetch-mode': 'cors',
    'sec-fetch-site': 'same-site',
    'user-agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/131.0.0.0 Safari/537.36',
    'x-sys-encode': '115992066215908888170874',
    'x-sys-terminal': '15986015651108888222042',
}

# 参数
telephones = "13301561910"
key = "C9144542C0704926ADC20A6A5AB69687"
base_url = "https://api.yoao.com/user/customer/getIndexCustomerPage"

# 生成 URL
final_url = generate_signature_and_url(telephones, key, base_url)

# 发起请求
response = requests.get(final_url, headers=headers)

# 输出结果
print("请求 URL:", final_url)
print("响应数据:", response.json())
with open("result.json","w")as f:
    json.dump(response.json(),f,ensure_ascii=False,indent=4)
