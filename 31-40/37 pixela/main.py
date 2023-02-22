import requests

username = 'jonathansires'
token = 'jonnysirespixela'

pixela_endpoint = f'https://pixe.la/v1/users'
graph_endpoint = f'https://pixe.la/v1/users/{username}/graphs'

user_params = {
    'token': 'jonnysirespixela',
    'username': 'jonathansires',
    'agreeTermsOfService': 'yes',
    'notMinor': 'yes',
}

# response = requests.post(url=pixela_endpoint, json=user_params)
# print(response.text)
graph_params = {
    'id': 'graph1',
    'name': 'sx',
    'unit': 'times',
    'type': 'int',
    'color': 'sora',
}

header = {
    'X-USER-TOKEN': token
}

response = requests.post(url=graph_endpoint, json=graph_params, headers=header)
print(response.text)