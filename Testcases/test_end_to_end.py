import requests
import json
import jsonpath
import pytest

def Testing_end_to_end():
    baseurl="https://thetestingworldapi.com/api/studentsDetails"

    file=open("C:/Users/kschandan/Desktop/pythonscripting/student.json","r")
    json_response=json.loads(file.read())
    response=requests.post(baseurl,json_response)
    id=jsonpath.jsonpath(json_response,"id")
    print(id[0])

    tech_api_url="https://thetestingworldapi.com/api/technicalskills"
    file = open("C:/Users/kschandan/Desktop/pythonscripting/student.json", "r")
    json_response = json.loads(file.read())
    response = requests.post(baseurl, json_response)
    id = jsonpath.jsonpath(json_response, "id")
    print(id[0])