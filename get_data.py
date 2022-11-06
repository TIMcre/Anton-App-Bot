import requests
import json
from datetime import datetime
from nested_lookup import nested_lookup
import re

url = ""

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
        return input(f"[{self.time()}] [{label}] {text}")


    
def get_json(url):
    try:
        data = requests.request("GET", url).json()
    except:
        console.write("Error", "invalid url")
        return None
    return data

def sort_json(data):
    qa_list = nested_lookup("b", data)   
    qa_list = re.sub("<.*?>|/d|\|+|\'|\"", "", str(qa_list)).strip("][").split(", ")
    return qa_list

def print_data(data):
    for item in data:
        console.write("output", item)

if __name__ == '__main__':
    console = Console()
    try:
        url = console.inp("Input", "Url: ")   
    except:
        console.write("Error", "invalid input")    
    data = get_json(url)
    data = sort_json(data)
    print_data(data)
    