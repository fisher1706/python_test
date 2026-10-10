from pprint import pprint
import requests


base_url = "https://mytest.ukrgasbank.com"


def get_token(login: str = "autotest", password: str = "Autotest1234!") -> str:
    url = f"{base_url}/api/customer/login"
    headers = {
        "Content-Type": "application/json"
    }
    payload = {
        "login": login,
        "password": password
    }

    pprint(requests.post(url=url, headers=headers, json=payload).json())
    print("\n")
    print("\n")
    print("\n")

    token = requests.post(url=url, headers=headers, json=payload).json()["value"]

    url = f"{base_url}/api/customer/sms-request"
    headers = {
        "Authorization": f"Bearer {token}",
        "Content-Type": "application/json",
    }
    pprint(requests.post(url=url, headers=headers).json())
    print("\n")
    print("\n")
    print("\n")

    url = f"{base_url}/api/customer/sms"
    headers = {
        "Authorization": f"Bearer {token}",
        "Content-Type": "application/json",
    }
    payload = {
        "code": 111111
    }
    pprint(requests.post(url=url, headers=headers, json=payload).json())
    print("\n")
    print("\n")
    print("\n")

    return token


def get_transaction_history():
    url = f"{base_url}/api/account/transaction-history"
    params = {
        "order": "desc",
        "sort": "executed,documentNumber",
        "size": 20,
        "page": 0,
        "accountIds": 229350,
        "dateFrom": "2026-04-13",
        "dateTo": "2026-04-19",
        "showZeroBalances": "false",
        "withRevaluation": "false",
        "showAdditionalDetails": "false",
        "time": "2026-04-23T17:34:10+03:00",
        "statuses": "EXECUTED",
        "withCurrencyTotals": "true",
        "withSync": "true",
        "forAll": "true"
    }
    headers = {
        "Authorization": f"Bearer {get_token()}",
        "Content-Type": "application/json"
    }

    return requests.get(url=url, headers=headers, params=params)


if __name__ == '__main__':
    resp = get_transaction_history()
    pprint(resp.json())

    print(resp.url)
