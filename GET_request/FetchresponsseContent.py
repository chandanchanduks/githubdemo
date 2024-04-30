import requests
import json
import jsonpath

url="https://reqres.in/api/users?page=2"

# API url

response=requests.get(url)
print(response) # used to print response code
print(response.content) # used to print response body
print(response.headers) # used to print response headers

print("\n")

# parse response to json format

response_body=json.loads(response.text)
print(response_body)

print("\n")

# Fetch value using JSON path

pages=jsonpath.jsonpath(response_body,'total_pages')
print(pages[0])