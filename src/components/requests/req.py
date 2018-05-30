# coding=utf-8

import requests

se = requests.session()
url = "http://test.api.user.huluxia.com/contacts/2.1?apk_id=102"
r = se.get(url)
print(r.json())

print(r.headers)
print(r.text)
print(r.cookies)
print(r.encoding)
print(r.status_code)
print(r.url)
print(r.ok)

print(type(r.cookies))

for x, y in r.cookies:
    print("%s -> %s" % (x, y))

requests.get("", header={})
