import requests as r

jose = r.post("https://api.2ip.me/geo.json?ip=138.199.21.207")
public = r.get("https://api.ipify.org?format=json")

data = public.text
print(data)