import requests
url = 'http://127.0.0.1:8000/api/v1/images/?id=1'
files = {'image': open('test.jpg', 'rb')}
headers = {'Authorization': 'Bearer 288859227179637902469712107280153584955'}
print(requests.get(url, headers=headers).json())

# url = 'http://127.0.0.1:8000/api/v1/delete_images/'
headers = {'Authorization': 'Bearer 288859227179637902469712107280153584955'}
# print(requests.post(url, headers=headers).json())

# print(requests.post(url, headers=headers, files=files))