import requests

res = requests.post("http://jadnik.com/user.php/",json={"username":"dovla","password":"123"}).json()

print(res)