import requests as req
resp = req.request(method='GET', url="http://3.210.117.131:3443/")
print(resp.text)
print(resp.status_code)
