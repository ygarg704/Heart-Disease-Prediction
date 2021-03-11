import requests

data = {'data': "67,1,4,160,286,0,2,108,1,1.5,2,3,3"}
r = requests.post("http://127.0.0.1:5000/predict", json=data)
print('response from server:', r)
