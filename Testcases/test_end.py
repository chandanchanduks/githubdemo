import requests
import json
import jsonpath
import pytest

def test_end_to_end():
    baseurl="https://thetestingworldapi.com/api/studentsDetails"

    file=open("C:/Users/kschandan/Desktop/New folder/studentsinfo.json","r")
    json_response=json.loads(file.read())
    response=requests.post(baseurl,json_response)
    id=jsonpath.jsonpath(json_response,"id")
    print(id[0])

    tech_api_url = "https://thetestingworldapi.com/api/technicalskills"
    file = open("C:/Users\kschandan\Desktop/New folder/techskills.json.json","r")
    json_response = json.loads(file.read())
    json_response["id"]=int(id[0])
    json_response["st_id"]=id[0]
    response = requests.post(tech_api_url, json_response)
    print(response.text)

    add_api_url = "https://thetestingworldapi.com/api/addresses"
    file = open("C:/Users/kschandan/Desktop/New folder/address.json","r")
    json_response = json.loads(file.read())
    json_response["id"] = int(id[0])
    json_response["st_id"] = id[0]
    response = requests.post(add_api_url, json_response)
    print(response.text)

    final_request="https://thetestingworldapi.com/api/FinalStudentDetails/"+str(id[0])
    response=requests.get(final_request)
    print(response.text)
