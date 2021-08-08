# https://www.youtube.com/watch?v=3Tm34b7p_cM&t=6s

import requests

headers = {
    "User-Agent": "zapel"
}

# response_1 = requests.get('https://httpbin.org/get', headers=headers, params={'a': 'b'})
# if response_1.status_code == 200:
#     print('ok')
#
# if response_1.ok:
#     print('ok')
#
# response_1.raise_for_status()
#
# print(response_1.text)
# print(response_1.json()['headers']['Host'])

response_2 = requests.post('https://httpbin.org/post',
                           headers=headers,
                           params={'a': 'b'},
                           json={'username': 'supersecret'}
                           )
print(response_2.text)
