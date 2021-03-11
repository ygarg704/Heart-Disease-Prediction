import requests

data = {'data': "67,1,4,160,286,0,2,108,1,1.5,2,3,3"}
r = requests.post("https://heart-predict.herokuapp.com/predict", json=data)
print('response from server:', r)
