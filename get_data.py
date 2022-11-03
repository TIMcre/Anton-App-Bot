import requests
import json
from nested_lookup import nested_lookup
import regex as re

url = "https://content.anton.app/files/?fileId=level%2Fc-mat-9%2Ftopic-01-wurzeln-und-potenzen%2Fblock-05-potenzgesetze%2Flevel-02&etag=d76b-4804"

def get_json(url):
    data = requests.request("GET", url).json()
    return data

def sort_json(data):
    question_list = []
    question_list = nested_lookup("b", data)
    re.sub("/ ^\< \>$/", "", question_list)
    return question_list

def print_data(data):
    for item in data:
        print(item,end="\n")

data = get_json(url)
data = sort_json(data)
print_data(data)