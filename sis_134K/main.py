import requests
from requests import Session
from getpass import getpass
import fake_user_agent
user = fake_user_agent.user_agent()
headers = {
    'user-agent': user
}

data = {
'request_type': 'RESPONSE',
'signInName': 'v363vc4',
'password': 'kD3y6WB4jE&_)Ym'

}
url = 'https://signin.cat.com/cwslogin.onmicrosoft.com/B2C_1A_P2_V1_SignIn_Prod/SelfAsserted?tx=StateProperties=eyJUSUQiOiIzNjk4MzBhMC0zYzkxLTRlZTgtOTM1NC02OWQwMDBjOTI5MmQifQ&p=B2C_1A_P2_V1_SignIn_Prod'
s = Session()
auth_response = s.post(url=url,headers=headers, data=data)
print(auth_response.text)
