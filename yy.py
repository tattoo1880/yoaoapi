import requests

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

response = requests.get(
    'https://api.yoao.com/user/customer/getIndexCustomerPage?customerTypes=116012874979938888848950,116268519059448888067837&mobile=18861613634&pageIndex=1&pageSize=10&sort=false&timestamp=1734078747&signature=D34ADD270EB1FD1EDD37AD503C08109A',
    headers=headers,
)

print(response.json())