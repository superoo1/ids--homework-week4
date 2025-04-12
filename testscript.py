import requests
for i in range(10000):
    con = requests.get("http://192.168.227.6:8000/", data="select")
    print(con.text)

