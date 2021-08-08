# https://www.youtube.com/watch?v=5_J2iQBArbQ&list=PLF4MWzDJPFSZbFLkfLnmy3zKQeyckCdKI&index=1
# https://www.youtube.com/watch?v=tTnquxuOUxc&list=PLF4MWzDJPFSZbFLkfLnmy3zKQeyckCdKI&index=2

import requests

# GET

page_1 = requests.get('http://google.com', params={
    # 'q': 'cats'
    'q': 'cats dogs pigs'
})
# print(page_1)
# print(page_1.status_code)
# print(page_1.content)
# print(page_1.content.decode(page_1.encoding))
# print(page_1.text)
print(page_1.url)
# print(page_1.headers)
# print(page_1.headers['Content-Type'])
#
# page_2 = requests.get('https://jsonplaceholder.typicode.com/posts/1')
# data = page_2.json()
#
# print(data)

# POST

website = 'https://jsonplaceholder.typicode.com/posts/1'
print(requests.get(website).json())

response_1 = requests.post(website, data={
    'userId': 12,
    'title': 'my new post',
    'body': 'body for my post',
    'photo': {'1.jpg', '2.jpg', '3.jpg'}
})

response_2 = requests.post(website, json={
    'userId': 12,
    'title': 'my new post',
    'body': 'body for my post'
})

# PUT
response_3 = requests.put(website, data={
    'userId': 12,
    'title': 'my new post',
    'body': 'body for my post zapel',
    'photo': {'1.jpg', '2.jpg', '3.jpg'}
})

# print(response_1.text)
# print(response_1.status_code)
#
# print(response_2.text)
# print(response_2.status_code)

# print(response_3.text)
print(response_3.status_code)
print(response_3.reason)
print(response_3.url)
print(response_3.json())
