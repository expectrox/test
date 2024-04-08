from requests.auth import HTTPBasicAuth
endpoint='http://mydomain.com/api/v1/auth'
user='juan'
password='not4passw0rD'
r = requests.post(endpoint, auth=HTTPBasicAuth(user, password), data=[])
