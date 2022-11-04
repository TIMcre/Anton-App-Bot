import requests
import json
from datetime import datetime
from nested_lookup import nested_lookup
import re

url = "https://content.anton.app/files/?fileId=level%2Fc-mat-9%2Ftopic-01-wurzeln-und-potenzen%2Fblock-05-potenzgesetze%2Flevel-test&etag=5594-3691"

#url = str(input("url"))

class Console:
    def __init__(self):
        pass

    def time(self):
        return datetime.now().time().strftime("%H:%M:%S")

    def clear(self):
        os.system("cls")

    def write(self, label: str, text: str):
        print(f"[{self.time()}] [{label}] {text}")

    def inp(self, label: str, text: str):
        pass


    
def get_json(url):
    try:
        data = requests.request("GET", url).json()
    except:
        console.write("Error", "invalid url")
        return None
    return data

def sort_json(data):
    question_list = []
    question_list = nested_lookup("b", data)    
    question_list = re.sub("<.*?>|/d|\|+|\'|\"", "", str(question_list)).strip("][").split(', ')
    return question_list

def print_data(data):
    for item in data:
        console.write("output", item)

console = Console()
data = get_json(url)
data = sort_json(data)
print_data(data)