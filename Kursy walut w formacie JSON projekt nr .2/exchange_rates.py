import requests
 
response = requests.get("https://cdn.kurs-walut.info/api/ecb.json")
 
if response.ok == True:
    data = response.json()
    rates = data["rates"]
    base = data["base"]
    putISODate = data["putISODate"]
 
    print("base: " + base)
    print("date: " + putISODate)
 
    for key in rates:
        print(key + ": ", rates[key])