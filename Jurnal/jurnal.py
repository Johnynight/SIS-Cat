import json
import pandas as pd
import openpyxl

import requests
from requests_ntlm2 import HttpNtlmAuth

s = requests.Session()

s.auth = HttpNtlmAuth('dnurgozhin', '1997Ndg1997')


url = 'http://eventjournalcrh.bmst-kz.borusan.com/Home/EventJournalGenerateExcel?json=[]'


r = s.get(url=url)

df = pd.read_excel(r.content,engine='openpyxl')
df.to_csv('data.csv')
# with open('jurnal.json', 'w',encoding='utf-8') as file:
#     json.dump(r.json(),file)

# ids = r.json()
# print('id count:', len(ids))
#
# i = 0
# data = []
# while ids[i:i+1000]:
#     print('requesting 1000 from', i)
#     r = s.post(
#         'http://eventjournalcrh.bmst-kz.borusan.com/Home/GetJournal',
#         json={'documentId': ids[i:i+1000]}
#     )
#     print(r.status_code)
#     data.extend(r.json())
#     i += 1000



