import requests
url = 'http://172.17.50.43/multi'
h = requests.head(url)
print("Header:")
print("**********")
for x in h.headers:
    print("\t ", x, ":", h.headers[x])

headers = {
    'User-Agent' : 'Mobile'
}
url2 = 'http://172.17.50.43/multi'
rh = requests.get(url2, headers=headers)
print(rh.text)