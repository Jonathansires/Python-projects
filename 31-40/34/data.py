import requests
from w3lib.html import replace_entities 
parameters = {
    "amount": 20,
    "type": "boolean",
    'category': '17'
}

response = requests.get(url='https://opentdb.com/api.php', params=parameters)
response.raise_for_status()

data = response.json()


question_data = (data['results'])
