import json
import requests
import jsonpath
import pytest

url="https://reqres.in/api/users"

def tests_second_user():
  response=requests.get(url)
  print(response.content)
  file=open("C:/Users/kschandan/Desktop/backup documents/New folder/Postrequest.json","r")
  json_input=file.read()
  request_json=json.loads(json_input)
  response=requests.post(url,request_json)
  assert response.status_code==201
  print(response.headers.get('content-length'))
  response_json=json.loads(response.text)
  id=jsonpath.jsonpath(response_json,"id")
  print(id[0])
