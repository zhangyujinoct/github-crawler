import datetime
import json
import requests
from myToken import my_token


def base_request(api, params):
    headers = {
        'Authorization': 'token ' + my_token,
        'accept': 'application/vnd.github.v3+json',
    }
    url = "https://api.github.com/" + api
    response = requests.get(url, headers=headers, params=params)
    return json.loads(response.content)
