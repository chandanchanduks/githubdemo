import json
import requests
import jsonpath

url="https://reqres.in/api/users"

#to get content of URL
response=requests.get(url)
print(response.content)

#read a file in json format

file=open("C:/Users/kschandan/Desktop/New folder/Postrequest.json","r")
json_input=file.read()
request_json=json.loads(json_input)

# make a post request with JSON body

response=requests.post(url,request_json)

# get status code

assert response.status_code==201

#fetch header from response

print(response.headers.get('content-length'))

# parse response to JSON format

response_json=json.loads(response.text)

# fetch id

id=jsonpath.jsonpath(response_json,"id")
print(id[0])




