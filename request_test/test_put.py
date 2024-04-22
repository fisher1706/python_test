# https://www.youtube.com/watch?v=tTnquxuOUxc&list=PLF4MWzDJPFSZbFLkfLnmy3zKQeyckCdKI&index=2


import requests

"""
PUT
"""

website = 'https://jsonplaceholder.typicode.com/posts/1'

response = requests.put(
    url=website,
    data={
        'userId': 12,
        'title': 'my new post',
        'body': 'body for my post zapel',
        'photo': {'1.jpg', '2.jpg', '3.jpg'}
        }
)

print(response)

if __name__ == '__main__':
    print(response.url)
    print(response.text)

    print(response.status_code)
    print(f'reason: {response.reason}')
    print(response.url)
    print(response.headers)
    print(response.json())
