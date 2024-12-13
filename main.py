import requests

headers = {
    'Host': 'app.dewu.com',
    'X-Auth-Token': 'Bearer eyJhbGciOiJSUzI1NiJ9.eyJpYXQiOjE3MzM3OTgwNDYsImV4cCI6MTc2NTMzNDA0NiwiaXNzIjoiVVVJRGQ1Y2Y2NGEyYzVlODQwMzNhYmMwNGMwMWUzZTcxYzNmIiwic3ViIjoiVVVJRGQ1Y2Y2NGEyYzVlODQwMzNhYmMwNGMwMWUzZTcxYzNmIiwidXVpZCI6IlVVSURkNWNmNjRhMmM1ZTg0MDMzYWJjMDRjMDFlM2U3MWMzZiIsInVzZXJJZCI6MjMzODEzODc0NiwidXNlck5hbWUiOiJOTDNFOSIsImlzR3Vlc3QiOmZhbHNlfQ.cbmE75kpIk6s0HIe59ey7MBuS8UBtyUN7Dkp0KS5SYPlq7pe9agfaxVn2Z__hXiqpWoyONSjXNdyMrwkLK0lFQIcsqDglmbfXL-qkZEiTDh3tgJDTMaAGSPvhcKyvc1huMZQP6GQN-cL79neFYLIyDqFMMPG9mszOBKlKqCwjG4vhEtlraVyK1Mp5_nMF9pDnsEvjnarJVPgBhI3TkwmyzlwzECEpOBkDKFJK3nF6uFlrepfZIUKIhIEaEXSQe4gAA8iaJ4sdPHSuEkipUqa-z3fHH7s3VfLs6Tm9ZnibT4pr1xdj1JHD1IPapqmWymJY44QhPaycVFw8PhLDGoCiw',
    'cookieToken': 'd1884a9820b553adfbf87473e7604d6ae8d91a2b36e76925976c7c3db12f09f22e7a5fd657e066b9fc544c0748ae472c9fe3982a0d229aed8c8ce58f67f2d2eca787182d469487a8f8178a2c69bd85a3|2338138746|1724942622|13c26473e5e954ddcde6618ee018032d9cd3f440|1-0|d41d8cd9e38b27b2',
    'loginToken': 'd1884a9820b553adfbf87473e7604d6ae8d91a2b36e76925976c7c3db12f09f22e7a5fd657e066b9fc544c0748ae472c9fe3982a0d229aed8c8ce58f67f2d2eca787182d469487a8f8178a2c69bd85a3|2338138746|1724942622|13c26473e5e954ddcde6618ee018032d9cd3f440|1-0|d41d8cd9e38b27b2',
    'brand': 'Apple',
    'appId': 'duapp',
    'isRoot': '0',
    'emu': '0',
    'Accept-Language': 'zh-Hans-CN;q=1.0',
    'app_build': '5.56.1.110',
    'isProxy': '1',
    'sks': '0,idw2',
    # 'ltk': 'edwtu1IfxoTl0Nz4uNQIgLFlRnigPDTKkcEBziNO1fl3OcSu94D1',
    'mode': '0',
    'v': '5.56.1',
    'dudeviceTrait': 'iPhone10,3',
    'timestamp': '1733799578322',
    # 'SK': '9OwPO9liODirg0nhlKYjh1UURrzQqikpLf9TS2RBM10PKnTEglybVXbdP5p7RFpqb4koMgfrUQnNYTKFce9UejkF7M1y',
    'platform': 'iPhone',
    'token': 'JLIjsdLjfsdII%3D%7CMTQxODg3MDczNA%3D%3D%7C07aaal32795abdeff41cc9633329932195',
    'webua': 'Mozilla/5.0 (iPhone; CPU iPhone OS 16_7 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Mobile/15E148',
    'shumeiid': '2024082922425286c8ccde0119e1e0cf5586d1b8226f9941b02fadf19bcb25',
    'edk': '7d7d616c355d5d414c6c3d6b6e3e3c693a6b3d6d303c383b3b696a6b383c6b38396d3b6d3f396b3b6e',
    'fcuuid': 'UUIDd5cf64a2c5e84033abc04c01e3e71c3f',
    'ipvx': '42.80.163.145',
    'Content-Type': 'application/x-www-form-urlencoded; charset=utf-8',
    # 'adi': 'Fdf3gpe3K3lUzVMZnEbz4pMKWZVERLXkFPLRC40Mi70=',
    'User-Agent': 'DUApp/5.56.1 (com.siwuai.duapp; build:5.56.1.110; iOS 16.7.0) DuNetClient/118.0.5953.0',
    # 'skc': 'txF69VuRHj7V1DJjMm434',
}

params = {
    'newSign': 'fc6b2e094068cab7523415b5ce7bdf8a',
}

data = {
    'timestamp': '1733799578322',
    'keyword': '长裤',
    'emu': '0',
    'isNewStruct': '1',
    'platform': 'iPhone',
    # 'sign': '0c7eb34a71892c5b1fc25d0f52e3e0df',
    'token': 'JLIjsdLjfsdII%3D%7CMTQxODg3MDczNA%3D%3D%7C07aaal32795abdeff41cc9633329932195',
    'app_build': '5.56.1.110',
    'v': '5.56.1',
    'isRoot': '0',
    'isProxy': '1',
    'cookieToken': 'd1884a9820b553adfbf87473e7604d6ae8d91a2b36e76925976c7c3db12f09f22e7a5fd657e066b9fc544c0748ae472c9fe3982a0d229aed8c8ce58f67f2d2eca787182d469487a8f8178a2c69bd85a3|2338138746|1724942622|13c26473e5e954ddcde6618ee018032d9cd3f440|1-0|d41d8cd9e38b27b2',
    'lastId': '5',
    'appId': 'duapp',
    # 'shumeiid': '2024082922425286c8ccde0119e1e0cf5586d1b8226f9941b02fadf19bcb25',
    # 'duid': '75f96163a9e719dfa889bd701fb84ddbab8268d022623cb518bb509a80bfe4c947d9c60d5e88b01898547bebad6bc13d',
    'brand': 'Apple',
    'loginToken': 'd1884a9820b553adfbf87473e7604d6ae8d91a2b36e76925976c7c3db12f09f22e7a5fd657e066b9fc544c0748ae472c9fe3982a0d229aed8c8ce58f67f2d2eca787182d469487a8f8178a2c69bd85a3|2338138746|1724942622|13c26473e5e954ddcde6618ee018032d9cd3f440|1-0|d41d8cd9e38b27b2',
    'mode': '0',
}

response = requests.post('https://app.dewu.com/sns-rec/v1/search/user-list', params=params, headers=headers, data=data)
print(response.json())