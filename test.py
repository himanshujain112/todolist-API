import requests

url = "http://127.0.0.1:3000/todo"

res = requests.get(url)

print(res.text)
#data = {"id": 13, "todo": "Learn Python"}
#res = requests.post(url, json=data)
#print(res.text)
#res = requests.get(url)
dataNew = requests.get(url)
print(dataNew[1] for i in dataNew)