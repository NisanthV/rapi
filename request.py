import requests

res=requests.post("http://localhost:8000/api/",json={"title":"createapi view"})
#res=requests.get("http://localhost:8000/api/7")
print(res.json())
