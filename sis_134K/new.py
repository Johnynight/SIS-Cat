import json
import requests
from requests.adapters import HTTPAdapter
from urllib3.util.retry import Retry
import urllib3
import urllib.parse
print('123')

urllib3.disable_warnings()

encodedUri = urllib.parse.quote("https://sis2.cat.com/", safe="")
with requests.Session() as session:
    r = session.get('https://sis2.cat.com/',verify=False, allow_redirects=False)
    correlationId = r.text[35:71]
    print(correlationId)
    r = session.get('https://sis2.cat.com/login?subapp=SIS&correlationId='+correlationId+'&intent='+encodedUri, allow_redirects=True, verify=False)
    headers = r.headers
    cookies = r.cookies
    r = session.post('https://signin.cat.com/', )
    print(r.text)