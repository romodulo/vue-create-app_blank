import requests
from pprint import pprint

request = requests.get("https://httpbin.org/get")
pprint(request.json())
print("")
pprint(dict(request.headers))
pprint(request.status_code)