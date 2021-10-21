import requests,threading,pandas

def atck():
	res=requests.get("https://www.hostalavenidas.com/")
	print(res)

for i in range(2000):
	threading.Thread(target=atck)






