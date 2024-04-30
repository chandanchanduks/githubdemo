import requests

url="https://reqres.in/api/users?page=2"

response=requests.get(url)

print(response.status_code)
print(response.content)
print(response.headers)





