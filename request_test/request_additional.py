# https://www.youtube.com/watch?v=IK448-nC8yU

import requests

# TODO: start proxy server first -> in command line - mitmproxy

"""
PROXY
"""

URL_PROXY = "https://ukr.net"

proxy = {
    "http": "http://localhost:8080",
    "https": "https://localhost:8080",
}

resp_proxy = requests.get(
    url=URL_PROXY,
    # proxies=proxy,
    # verify=False
)


"""
COOKIES
"""

URL_COOKIES = "https://www.ukr.net"

headers = {"Cookie": "uid=Cj1tBGD/uaVp4eoZBpTMAg==; snr=9"}

cookies = {"uid": "Cj1tBGD/uaVp4eoZBpTMAg==", "snr": "9"}

resp_headers = requests.get(URL_COOKIES, headers=headers)

resp_cookies = requests.get(url=URL_COOKIES, cookies=cookies)


"""
REDIRECT/TIMEOUT
"""


URL_REDIRECT_ONE = "https://httpbin.org/redirect/3"
URL_REDIRECT_TWO = "https://httpbin.org/absolute-redirect/3"

resp_redirect_one = requests.get(url=URL_REDIRECT_ONE)

resp_redirect_timeout = requests.get(url=URL_REDIRECT_TWO, timeout=1)

resp_redirect_forbidden = requests.get(url=URL_REDIRECT_TWO, allow_redirects=False)


"""
DOWNLOAD
"""

URL_DOWNLOAD = "https://ukr.net"
URL_DOWNLOAD_LAGE = (
    "https://www.shutterstock.com/blog/india/wp-content/uploads/sites/10/2018/04/"
    "freestock_2991094.jpg?resize=1250,1120"
)
URL_UPLOAD = "https://httpbin.org/anything"


def open_download_content(url=URL_DOWNLOAD):
    resp = requests.get(url=url)

    with open("download_folder/index.html", "wb") as f:
        f.write(resp.content)


def upload_downloaded_big_image(url_download=URL_DOWNLOAD_LAGE, url_upload=URL_UPLOAD):
    resp = requests.get(url=url_download, stream=True)

    with open("download_folder/index.jpg", "wb") as f:
        for chunk in resp.iter_content(chunk_size=1024):
            print("CHUNK!")
            f.write(chunk)

    with open("download_folder/index.jpg", "rb") as f:
        requests.post(url=url_upload, data=f)


if __name__ == "__main__":
    # print(resp_proxy.status_code)
    # print("*" * 200)

    # print(resp_headers.cookies.items())
    # print(resp_cookies.cookies.items())
    # print("*" * 200)
    #
    # print(resp_redirect_one.history)
    # print(resp_redirect_timeout.history)
    # print(resp_redirect_forbidden.history)
    # print("*" * 200)

    # open_download_content()
    upload_downloaded_big_image()
