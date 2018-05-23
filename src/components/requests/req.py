# coding=utf-8

import requests

r = requests.get("http://test.api.user.huluxia.com/contacts/2.1?apk_id=102")
print(r.json())
