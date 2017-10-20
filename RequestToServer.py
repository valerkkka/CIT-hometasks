import requests
import json

main_url = 'http://cit-home1.herokuapp.com'
register_url = '/api/register'
check_url = '/api/check_me'

data = {'message': 'Hello, my name is Lera'}
headers = {'content-type': 'application/json'}

req = requests.post(main_url + register_url, data=json.dumps(data), headers=headers)
print("Status code is " + str(req.status_code))
print(req.json())

req = requests.get(main_url + check_url)
print(req.json())