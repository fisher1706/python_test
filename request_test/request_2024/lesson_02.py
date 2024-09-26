from pprint import pprint

import requests
from requests.auth import HTTPBasicAuth


resp_1 = requests.get(
    url="https://petstore.swagger.io/v2/store/inventory",
    headers={"api_key": "special-key"},
    # params={},
    # verify=False
    # auth=HTTPBasicAuth('user', 'password'),
)

print(resp_1.json())
print(resp_1.status_code)
print(resp_1.headers)


resp_2 = requests.get(
    url="https://petstore.swagger.io/v2/pet/findByStatus",
    headers={"api_key": "special-key"},
    params={
        "status": "sold",
    },
)

pprint(resp_2.json())
