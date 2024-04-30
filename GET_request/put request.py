import requests
import json
import jsonpath

url="https://reqres.in/api/users/2"

#open a file

file=open("C:/Users/kschandan/Desktop/New folder/Postrequest.json","r")
json_input=file.read()
response_json=json.loads(json_input)

#make a put request with json body

response=requests.put(url,response_json)

#get status code

assert response.status_code==200

#get header

print(response.headers.get("content-length"))

#parse response into json format

response_json=json.loads(response.text)

#fetch id

updatedAt=jsonpath.jsonpath(response_json,'updatedAt')
print(updatedAt[0])


