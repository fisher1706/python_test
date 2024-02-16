# https://www.youtube.com/watch?v=3Tm34b7p_cM&t=6s

import requests

URL_GET = 'https://httpbin.org/get'
URL_POST = 'https://httpbin.org/post'

headers = {
    "User-Agent": "zapel"
}

"""
GET
"""

resp_get = requests.get(
    url=URL_GET,
    headers=headers,
    params={
        'a': 'b',
        'c': 'd'
    }
)

"""
POST
"""

resp_post = requests.post(
    url=URL_POST,
    headers=headers,
    params={'a': 'b'},
    json={'username': 'supersecret'}
)

if __name__ == '__main__':
    if resp_get.status_code == 200:
        print('ok')

    if resp_get.ok:
        print('ok')

    print(resp_get.raise_for_status())
    print(resp_get.text)
    print(resp_get.json()['headers']['Host'])
    print(resp_get.json()['headers'])

    print(resp_post.json())
