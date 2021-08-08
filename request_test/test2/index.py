import requests
# PROXY
# proxy = {'http': 'localhost:8080', 'https': 'localhost:8080'}
proxy = {'http': 'localhost:8080'}

# requests.get('http://ukr.net', proxies=proxy, verify=False)
# requests.get('https://ukr.net', proxies=proxy, verify=False)

# COOKIES
# ukr = 'http://www.ukr.net'
#
# headers = {'Cookie': 'uid=Cj1tBGD/uaVp4eoZBpTMAg==; snr=9'}
#
# cookies = {'uid': 'Cj1tBGD/uaVp4eoZBpTMAg==',
#            'snr': '9'}

# r = requests.get(ukr,  proxies=proxy, headers=headers, verify=False)
# r = requests.get(ukr,  proxies=proxy, cookies=cookies, verify=False)
# print(r.cookies.items())

# REDIRECT/TIMEOUT

hbin = 'http://httpbin.org/redirect/1'
# hbin = 'http://httpbin.org/absolute-redirect/1'

# r = requests.get(hbin, proxies=proxy)
# r = requests.get(hbin, proxies=proxy, timeout=1)
# r = requests.get(hbin, proxies=proxy, allow_redirects=False)

# print(r.history)

ukr = 'http://ukr.net'
large = 'https://www.facebook.com/photo/?fbid=4440947052624918&set=a.695471223839205'




# r = requests.get(ukr, proxies=proxy, verify=False)
#
# with open('index.html', 'wb') as f:
#     f.write(r.content)


# r1 = requests.get(large, proxies=proxy, verify=False, stream=True)
# with open('index.jpg', 'wb') as f:
#     for chunk in r1.iter_content(chunk_size=1024):
#         print('CHUNK!')
#         f.write(chunk)

upload = 'http://httpbin.org/anything'

with open('index.jpg', 'rb') as f:
    requests.post(upload, proxies=proxy, data=f)


